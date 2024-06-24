import logging
from sqlalchemy import create_engine, text, StaticPool
from sqlalchemy.orm import Session

from app.db.session import DbSession

from app.config import get_config
from app.db.models.base import Base

logger = logging.getLogger(__name__)


class Database:
    def __init__(self, dsn: str):
        try:
            if "sqlite://" in dsn:
                self.engine = create_engine(
                    dsn,
                    connect_args={'check_same_thread': False},      # This + static pool is needed for sqlite in-memory tables
                    poolclass=StaticPool
                )
            else:
                config = get_config()
                self.engine = create_engine(
                    dsn,
                    echo=False,
                    pool_pre_ping=config.database.pool_pre_ping,
                    pool_recycle=config.database.pool_recycle,
                    pool_size=config.database.pool_size,
                    max_overflow=config.database.max_overflow
                )
        except BaseException as e:
            logger.error("Error while connecting to database: %s", e)
            raise e

    def generate_tables(self) -> None:
        logger.info("Generating tables...")
        Base.metadata.create_all(self.engine)

    def is_healthy(self) -> bool:
        """
        Check if the database is healthy

        :return: True if the database is healthy, False otherwise
        """
        try:
            with Session(self.engine) as session:
                session.execute(text('SELECT 1'))
            return True
        except Exception as e:
            logger.info("Database is not healthy: %s", e)
            return False

    def get_db_session(self) -> DbSession:
        return DbSession(self.engine)
