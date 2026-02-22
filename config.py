from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application configuration settings.
    Values can be overridden via environment variables or a .env file.
    """

    # App Info
    app_name: str = "FastAPI Beginner's Toolkit"
    app_version: str = "1.0.0"
    app_description: str = (
        "A beginner-friendly FastAPI application built for the Moringa AI Capstone Project."
    )

    # Server
    host: str = "127.0.0.1"
    port: int = 8000
    debug: bool = True
    reload: bool = True

    # API
    api_prefix: str = "/api/v1"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Single instance to be imported across the app
settings = Settings()
