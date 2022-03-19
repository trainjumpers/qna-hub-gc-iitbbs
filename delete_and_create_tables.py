#!/usr/bin/python3
"""
This file will drop all existing tables and recreate them from scratch. Meant for testing purposes
"""

import asyncio
import os

import asyncpg
from dotenv import load_dotenv


async def drop_all_tables(connection):
    query = f"""SELECT tablename FROM pg_tables WHERE schemaname = '{schema_name}';"""
    print(f"Executing query: {query}")
    result = await connection.fetch(query)

    tables = [f"{schema_name}.{row['tablename']}" for row in result]
    tables = ', '.join(tables)
    query = f"DROP TABLE IF EXISTS {tables} CASCADE;"
    print(f"Executing query: {query}")
    await connection.execute(query)


async def create_user_table(connection):
    query = f"""CREATE TABLE {schema_name}.user (
        id              SERIAL PRIMARY KEY,
        name            VARCHAR(64) NULL,
        email           VARCHAR(64) UNIQUE NOT NULL,
        hashed_password VARCHAR(128) NOT NULL,
        role            SMALLINT NULL,
        is_verified     BOOLEAN NOT NULL DEFAULT false,
        created_at      TIMESTAMP NOT NULL DEFAULT now(),
        is_active       BOOLEAN NOT NULL DEFAULT true,
        is_deactivated  BOOLEAN NOT NULL DEFAULT false
    );"""

    print(f"Executing query: {query}")
    result = await connection.execute(query)
    print("Result", result)


async def create_connection():
    return await asyncpg.connect(
        host=os.environ.get('DB_HOST'),
        port=os.environ.get('DB_PORT'),
        database=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        timeout=int(os.environ.get('CONNECTION_TIMEOUT', 10)),
        command_timeout=int(os.environ.get('QUERY_TIMEOUT', 60)),
    )


async def rebuild_schema():
    connection = await create_connection()

    print(f"Dropping all tables in schema: {schema_name}")
    await drop_all_tables(connection)
    print(f"Dropped all tables in schema: {schema_name}")

    print(f"Recreating all tables in schema: {schema_name}")
    await create_user_table(connection)

    await connection.close()



load_dotenv()

host_name = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')
schema_name = os.environ.get('DB_SCHEMA')

asyncio.get_event_loop().run_until_complete(rebuild_schema())
