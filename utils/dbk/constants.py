#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/4 00:13
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   constants.py
# @Desc     :

from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
SQLITE: Path = BASE / "data/sqlite3.db"

if __name__ == "__main__":
    path: Path = Path(SQLITE)
    print(path.exists())
