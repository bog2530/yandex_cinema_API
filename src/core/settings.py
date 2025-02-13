from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    class Config:
        env_file = ".env"

    PROJECT_NAME: str = "movies"
    PATH_PREFIX: str = "/api"
    CORS_ALLOWED_ORIGINS: list[str] = ["*"]

    REDIS_HOST: str = "127.0.0.1"
    REDIS_PORT: int = 6379

    ELASTIC_HOST: str = "127.0.0.1"
    ELASTIC_PORT: int = 9200
    ELASTIC_SCHEMA: str = ""


settings = Settings()
