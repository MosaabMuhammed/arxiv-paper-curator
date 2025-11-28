from pydantic import BaseModel


class PostegresSettings(BaseModel):
    DATABASE_URL: str = "postgresql://rag_user:rag_password@localhost:5432/rag_db"
    ECHO_SQL: bool = False
    POOL_SIZE: int = 20
    MAX_OVERFLOW: int = 0
