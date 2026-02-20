from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn, field_validator, AnyHttpUrl


class Settings(BaseSettings):
    PROJECT_NAME: str = "FlowMind API"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: PostgresDsn
    SQL_ECHO: bool = False  # Set to True for SQL debug output; keep False in production

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    
    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: str | List[str]) -> List[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding='utf-8',
        case_sensitive=True, # Avoid typos in the .env file
        extra="ignore"       # Avoid crashing if you add comments or extra vars to the .env file
    )

settings = Settings()