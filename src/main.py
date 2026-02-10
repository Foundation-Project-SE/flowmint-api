from fastapi import FastAPI

app = FastAPI(
    title="Foundation Backend",
    description="Hexagonal API Foundation team project",
    version="0.1.0",
)

@app.get("/health")
async def health_check():
    return {"status": "ok",
            "architecture": "hexagonal"}