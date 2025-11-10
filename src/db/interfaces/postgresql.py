from contextlib import contextmanager
from typing import Generator, Optional

from loguru import logger
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from src.db.interfaces.base import BaseDatabase
from src.settings import default_settings

Base = declarative_base()


class PostgreSQLDB(BaseDatabase):
    """PostgreSQL DB implementation."""

    def __init__(
        self,
        database_url: str = default_settings.POSTGRES.DATABASE_URL,
        echo_sql: bool = default_settings.POSTGRES.ECHO_SQL,
        pool_size: int = default_settings.POSTGRES.POOL_SIZE,
        max_overflow: int = default_settings.POSTGRES.MAX_OVERFLOW,
    ):
        self.database_url = database_url
        self.echo_sql = echo_sql
        self.pool_size = pool_size
        self.max_overflow = max_overflow
        self.engine: Optional[Engine] = None
        self.session_factory: Optional[sessionmaker] = None

    def startup(self) -> None:
        """Initialize the database connection."""

        try:
            logger.info(
                "Attempting to connect to PostgreSQL at: {connection}",
                connection=self.database_url.split("@")[1] if "@" in self.database_url else "localhost",
            )

            self.engine = create_engine(
                self.database_url,
                echo=self.echo_sql,
                pool_size=self.pool_size,
                poo_pre_ping=True,  # Verify connections before use
            )

            self.session_factory = sessionmaker(bind=self.engine, expire_on_commit=False)

            # --- Test connection ---
            self._test_connection()

            # --- Create tables (idempotent) ---
            new_tables = self._create_missing_tables()

            logger.success("PostgreSQL database initialized successfully ✅")
            logger.info("Database: {db}", db=self.engine.url.database)
            logger.info(f"New tables created: {', '.join(new_tables)}" if new_tables else "No new tables created")
        except SQLAlchemyError as e:
            logger.error(f"SQLAlchemy error during DB initialization")
            raise
        except Exception as e:
            logger.exception(f"Unexpected error initializing database")
            raise

    def _test_connection(self) -> None:
        """Run a test query to confirm DB connectivity."""
        if not self.engine:
            raise RuntimeError("Engine not initialized before testing connection.")

        with self.engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            if result.scalar() == 1:
                logger.info("Database connection test successful 🟢")
            else:
                logger.warning("Database connection test returned unexpected result.")

    def _create_missing_tables(self) -> set[str]:
        """Create tables if they don't exist and return any newly created ones."""
        inspector = inspect(self.engine)
        before = set(inspector.get_table_names())

        Base.metadata.create_all(bind=self.engine)

        after = set(inspector.get_table_names())
        new_tables = after - before
        return new_tables

    def teardown(self) -> None:
        """Close the database connection."""
        if self.engine:
            self.engine.dispose()
            logger.info("PostgreSQL database connection closed.")

    @contextmanager
    def get_session(self) -> Generator[Session, None, None]:
        """Get a database session."""
        if not self.session_factory:
            raise RuntimeError("Database not initialized. Call startup() first!")

        session = self.session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
