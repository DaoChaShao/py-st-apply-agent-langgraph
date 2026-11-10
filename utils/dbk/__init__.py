#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/3 23:56
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   __init__.py.py
# @Desc     :

"""
****************************************************************
Database Core - Database Management Toolkit
----------------------------------------------------------------
This package provides a collection of reusable utilities, classes,
and components for database configuration, connection management,
session handling, transaction control, and data access.

Designed to provide a modular, extensible, and consistent interface
for database operations across different database systems.
****************************************************************
"""

__author__ = "Shawn Yu"
__version__ = "0.1.0"

from .base import DECLARATION
from .configs import DBConfig
from .constants import SQLITE
from .engines import InitEngine
from .models import Exercise
from .repository import (
    check_table_exists,
    count_data,
    create_db,
    delete_data,
    drop_db,
    eliminate_db,
    get_data,
)
from .session import InitSession

__all__ = [
    "DECLARATION",

    "DBConfig",

    "SQLITE",

    "InitEngine",

    "Exercise",

    "check_table_exists",
    "count_data",
    "create_db",
    "delete_data",
    "drop_db",
    "eliminate_db",
    "get_data",

    "InitSession",
]
