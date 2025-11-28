from loguru import logger

from src.db.interfaces.base import BaseDatabase
from src.db.interfaces.postgresql import PostgreSQLDB


def make_database() -> BaseDatabase:
    """
    Factory function to create a database instance.

    Returns:
        BaseDatabase: An instance of the database.

    Raises:
        RuntimeError: If database initialization fails.
    """
    try:
        db = PostgreSQLDB()
        db.startup()
        return db
    except Exception as e:
        logger.error(f"Database factory failed: {e}")
        raise RuntimeError(f"Failed to create database instance: {e}") from e
