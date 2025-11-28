from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

from .ollama_settings import OllamaSettings
from .opensearch_settings import OpenSearchSettings
from .postgres_settings import PostegresSettings


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", frozen=True, env_nested_delimiter="__")

    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    SERVICE_NAME: str = "rag-api"

    POSTGRES: PostegresSettings
    OLLAMA: OllamaSettings
    OPENSEARCH: OpenSearchSettings


@lru_cache
def get_settings() -> Settings:
    """Get application settings."""
    return Settings()


settings = Settings()
