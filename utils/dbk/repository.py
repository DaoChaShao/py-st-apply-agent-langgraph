#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/7 16:00
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   repository.py
# @Desc     :

from os import remove
from pathlib import Path
from typing import Any

from pandas import DataFrame, read_sql
from sqlalchemy import inspect
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from .base import DECLARATION


def check_table_exists(engine: Engine, table: str, *, display: bool = False) -> bool:
    """
    Check if the table exists in the database

    :param engine: The database engine
    :param table: The table name
    :param display: Display the table names in the database
    :return: True if the table exists, otherwise False
    """
    inspector = inspect(engine)
    if display:
        print(inspector.get_table_names())
    return table in inspector.get_table_names()


def count_data(session: Session, table: Any) -> int:
    """
    Count the number of the table in the database

    :param session: The database session
    :param table: The table name
    :return: The number of the table in the database
    """
    return session.query(func.count(table.id)).scalar()


def create_db(engine: Engine) -> None:
    """
    Create a database

    :param engine: The database engine
    :return: None
    """
    DECLARATION.metadata.create_all(engine.engine)


def delete_data(session: Session, table: Any) -> None:
    """
    Delete the data in the table

    :param session: The database session
    :param table: The table object
    :return: None
    """
    session.query(table).delete()
    session.commit()


def drop_db(engine: Engine) -> None:
    """
    Drop a database

    :param engine: The database engine
    :return: None
    """
    DECLARATION.metadata.drop_all(engine)


def eliminate_db(engine: Engine, db_path: Path, *, display: bool = False) -> None:
    """
    Eliminate a database

    :param engine: The database engine
    :param db_path: The database path
    :param display: Display the message
    :return: None
    """
    engine.dispose()

    if db_path.exists():
        remove(db_path)
        if display:
            print(f"Database '{db_path.name}' eliminated successfully.")


def get_data(session: Session, table: Any) -> DataFrame:
    """
    Get the data from the table

    :param session: The database session
    :param table: The table object
    :return: The data from the table
    """
    statement = session.query(table).statement
    return read_sql(statement, session.bind)
