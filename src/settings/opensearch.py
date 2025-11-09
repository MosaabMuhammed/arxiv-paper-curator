from pydantic import BaseModel


class OpenSearchSettings(BaseModel):
    HOST: str = "http://localhost:9200"
