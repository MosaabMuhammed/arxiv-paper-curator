from src.db.interfaces.base import BaseDatabase
from src.db.interfaces.postgresql import PostgreSQLDB


def make_database() -> BaseDatabase:
    """
    Factory function to create a database instance.

    Returns:
        BaseDatabase: An instance of the database.
    """
    db = PostgreSQLDB()
    db.startup()
    return db
