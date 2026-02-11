import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Required variables (without default value)
    DATABASE_URL: str
    
    # Default variables values
    PROJECT_NAME: str = "FlowMind API"
    API_V1_STR: str = "/api/v1"
    
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding='utf-8',
        case_sensitive=True, # Avoid typos in the .env file
        extra="ignore"       # Avoid crashing if you add comments or extra vars to the .env file
    )

settings = Settings()