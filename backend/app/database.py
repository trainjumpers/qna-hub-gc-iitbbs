from os import environ

import asyncpg
from asyncpg import create_pool

from app.utils.logging import logger


class DatabaseConnectionPool:
    """Singleton for PostgreSQL database connection pool which holds an instance of a connection pool and shares that 
    same instance with all the access invocations. It is instantiated in the main.py file via create_connection_pool()
    Class attributes:
        instance: an instance of the class asyncpg.Pool
    """

    instance: asyncpg.Pool = None

    def __init__(self):
        raise NotImplementedError(f"DatabaseConnectionPool cannot be instantiated")

    @classmethod
    async def create_connection_pool(cls):
        """Initialises the shared instance variable holding the connection pool for the Postgres database.
        """

        if cls.instance:
            logger.info("Database connection pool instance already initialised")
            return

        logger.info("Creating database connection pool instance")
        cls.instance = await create_pool(
            host=environ.get('DB_HOST', 'localhost'),
            port=environ.get('DB_PORT', 5432),
            database=environ.get('DB_NAME', 'testdb'),
            user=environ.get('DB_USER', 'testuser'),
            password=environ.get('DB_PASSWORD', 'test'),
            min_size=5,
            max_size=100,
            timeout=int(environ.get('CONNECTION_TIMEOUT', 10)),
            command_timeout=int(environ.get('QUERY_TIMEOUT', 60)),
            max_inactive_connection_lifetime=480,
        )

    @classmethod
    def get_connection_pool(cls):
        """Returns the connection pool instance.
        Raises:
            ValueError: if the connection pool instance has not been initialised before being requested for
        """

        logger.info("Acquiring database connection pool instance")
        if not cls.instance:
            raise ValueError("Connection pool instance was not initialised on application startup")
        return cls.instance

    @classmethod
    async def close_connection_pool(cls):
        """Closes all open and active connections in the connection pool.
        """

        logger.info(f"Closing all connections in the connection pool")
        await cls.instance.close()