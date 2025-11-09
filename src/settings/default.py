from typing import List, Union

from ollama import OllamaSettings
from opensearch import OpenSearchSettings
from postgres import PostegresSettings
from pydantic_settings import BaseSettings, SettingsConfigDict


class DefaultSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", frozen=True, env_nested_delimiter="__")

    APP_VESION: str = "0.1.0"
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    SERVICE_NAME: str = "rag-api"

    POSTGRES: PostegresSettings
    OLLAMA: OllamaSettings
    OPENSEARCH: OpenSearchSettings


def get_settings() -> DefaultSettings:
    """Get application settings."""
    return DefaultSettings()
