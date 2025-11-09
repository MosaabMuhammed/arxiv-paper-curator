from typing import List, Union

from pydantic import BaseModel, Field, field_validator


class OllamaSettings(BaseModel):
    HOST: str = "http://localhost:11434"
    MODELS: Union[str, List[str]] = Field(default=["gpt-oss:20b", "llama3.2:1b"])
    DEFAULT_MODEL: str = "llama3.2:1b"
    TIMEOUT: int = 300

    @field_validator("MODELS", mode="before")
    @classmethod
    def parse_ollama_models(cls, v):
        """parse comma-separated string into list of models."""
        if isinstance(v, str):
            return [model.strip() for model in v.split(",") if model.strip()]
        return v
