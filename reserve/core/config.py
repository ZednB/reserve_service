from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    POSTGRES_URL: PostgresDsn = "postgresql://postgres:1111@localhost:5432/reserver_service"

    class Config:
        env_file = '.env'


settings = Settings()
