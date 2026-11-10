#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/4 00:01
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   engines.py
# @Desc     :

from sqlalchemy import Engine, create_engine, event

from ..helper import Access
from .configs import DBConfig


class InitEngine(Access):
    """ Initialise Engine with SQLAlchemy """

    def __init__(self, config: DBConfig) -> None:
        """ Configure SQLite3 settings """
        self._engine = create_engine(
            config.url,
            echo=config.echo,
            connect_args={
                "timeout": config.timeout,
            },
        )

        self._configure_sqlite()

    def _configure_sqlite(self) -> None:
        """ Configure foreign keys for SQLite """

        @event.listens_for(self._engine, "connect")
        def set_sqlite_pragma(dbapi_connection, _):
            if "sqlite3" in str(type(dbapi_connection)):
                cursor = dbapi_connection.cursor()
                cursor.execute("PRAGMA foreign_keys=ON")
                cursor.close()

    def dispose(self) -> None:
        """ Dispose the engine """
        self._engine.dispose()

    @property
    def engine(self) -> Engine:
        """ Return the engine """
        return self._engine


if __name__ == "__main__":
    pass
