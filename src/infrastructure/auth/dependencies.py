from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# HTTPBearer tells to FastAPI (and to Swagger/OpenAPI) that this route 
# needs a "Bearer" token in the headers.
security = HTTPBearer()

def get_current_user_id_stub(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    """
    MVP STUB: Temporary Authentication Adapter.
    In the future, this function will take the credentials.credentials (the JWT token),
    verify it against Supabase, and extract the real user ID.
    
    For now, simply validate that you send "something" and return a hardcoded user ID.
    """
    token = credentials.credentials
    
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication token missing",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # HERE IS THE STUB: If we send the magic test token, we let them pass.
    if token == "test-token-mvp":
        return "123e4567-e89b-12d3-a456-426614174000" # A test UUID simulating Supabase
        
    # If they send something else, we reject them.
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token (Stub mode)",
        headers={"WWW-Authenticate": "Bearer"},
    )