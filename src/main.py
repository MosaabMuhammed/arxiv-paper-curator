import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger
from src.db.factory import make_database
from src.settings import default_settings

# from src.routers import ask, papers, ping


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting RAG API...")

    app.state.settings = default_settings

    db = make_database()
    app.state.db = db
    logger.info("Database connected!")

    # Placeholder for future weeks
    app.state.pdf_parser_service = None
    app.state.opensearch_service = None
    app.state.llm_service = None

    logger.info("API ready")
    yield

    # Cleanup
    db.teardown()
    logger.info("API shutdown complete")


app = FastAPI(
    title="arXiv Paper Curator API",
    description="Personal arXiv CS.AI paper curator with RAG cababilities",
    version=default_settings.APP_VERSION,
    root_path="/api/v1",
    lifespan=lifespan,
)

if __name__ == "__main__":
    import uvicorn

    host = "0.0.0.0" if default_settings.ENVIRONMENT == "production" else "127.0.0.1"  # nosec B104
    uvicorn.run(app, port=8000, host=host)  # nosec B104
