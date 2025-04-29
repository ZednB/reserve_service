from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    POSTGRES_URL: str = Field(
        default="postgresql://postgres:1111@localhost:5432/reserve_service",
        env="POSTGRES_URL"
    )

    class Config:
        env_file = ".env"
        extra = "ignore"  # Игнорировать лишние переменные


settings = Settings()
