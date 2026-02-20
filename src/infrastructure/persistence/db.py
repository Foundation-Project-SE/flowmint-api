from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from src.infrastructure.config import settings

# 1. Engine
# Physical connection with db. echo=True shows SQL on console for debugging (configure via SQL_ECHO)
engine = create_async_engine(
    str(settings.DATABASE_URL),
    echo=settings.SQL_ECHO,
    future=True,
    connect_args={"statement_cache_size": 0}    # This line solves de PgBouncer technology on Transaction Pooler of supabase
                                                # Turning off the cache allows to use shared connections (Transaction Pooler)
)

# 2. Sessions factory
# Engine don't get used directly. It's used by "Sesions".
# Each session, is a temporary "box of changes" for a transaction
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False, # Note: this avoids objects disconnection on saving
    autoflush=False
)

# 3. Base Class (DeclarativeBase)
# Every models (Users, Transactions) Inherit from this class.
# This allows SQLAlchemy knows wich tables exists.
class Base(DeclarativeBase):
    pass

# 4. FastAPI Dependency (Dependency Injection)
# This functions will be used on routes, for example: @app.get("/", db: AsyncSession = Depends(get_db))
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session               # Delivers session to endpoint
            await session.commit()      # If everything is allright, save changes (Commit)
        except Exception:
            await session.rollback()    # If there is an error, undo changes (Rollback)
            raise
        finally:
            await session.close()       # Always close connection