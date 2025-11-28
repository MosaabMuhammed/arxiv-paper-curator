import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger

from src.db.factory import make_database
from src.routers import ask_router, papers_router, ping_router
from src.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting RAG API...")

    app.state.settings = settings

    # Initialize database with error handling
    try:
        db = make_database()
        app.state.db = db
        logger.info("Database connected!")
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        raise

    # Placeholder for future weeks
    app.state.pdf_parser_service = None
    app.state.opensearch_service = None
    app.state.llm_service = None

    logger.info("API ready")
    yield

    # Cleanup
    try:
        db.teardown()
        logger.info("Database connection closed")
    except Exception as e:
        logger.error(f"Error during database cleanup: {e}")

    logger.info("API shutdown complete")


app = FastAPI(
    title="arXiv Paper Curator API",
    description="Personal arXiv CS.AI paper curator with RAG cababilities",
    version=settings.APP_VERSION,
    root_path="/api/v1",
    lifespan=lifespan,
)

# Include routers
app.include_router(ping_router.router)
app.include_router(papers_router.router)
app.include_router(ask_router.router)
