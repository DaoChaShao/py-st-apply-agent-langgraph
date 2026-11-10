#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/5 22:06
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   session.py
# @Desc     :

from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from ..helper import Access


class InitSession(Access):
    """ Initialise Session """

    def __init__(self, engine: Engine) -> None:
        """ Initialise Session """
        self._session = sessionmaker(
            bind=engine,
            autoflush=False,
            expire_on_commit=False,
        )

    def init(self) -> Session:
        """ Initialise Session """
        return self._session()
