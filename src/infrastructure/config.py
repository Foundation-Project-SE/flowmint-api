from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn, field_validator, model_validator, AnyHttpUrl


class Settings(BaseSettings):
    PROJECT_NAME: str = "FlowMind API"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: PostgresDsn
    SQL_ECHO: bool = False  # Set to True for SQL debug output; keep False in production

    # Environment: "dev" | "prod" | etc. Used to disable stub auth in production.
    APP_ENV: str = "dev"

    # Stub auth (MVP): when enabled, accepts STUB_AUTH_TOKEN and returns STUB_AUTH_USER_ID.
    # Default: True if APP_ENV != "prod", False in prod. Override with env var.
    STUB_AUTH_ENABLED: bool | None = None
    STUB_AUTH_TOKEN: str = ""
    STUB_AUTH_USER_ID: str = ""

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    
    @model_validator(mode="after")
    def set_stub_auth_default(self) -> "Settings":
        if self.STUB_AUTH_ENABLED is None:
            return self.model_copy(
                update={"STUB_AUTH_ENABLED": self.APP_ENV.lower() != "prod"}
            )
        return self

    def is_stub_auth_enabled(self) -> bool:
        """Effective stub auth: False in prod, otherwise STUB_AUTH_ENABLED."""
        if self.APP_ENV.lower() == "prod":
            return False
        return bool(self.STUB_AUTH_ENABLED)

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