#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/4 00:01
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   configs.py
# @Desc     :

from dataclasses import dataclass
from pathlib import Path


@dataclass
class DBConfig:
    path: Path
    echo: bool = False
    timeout: int = 30

    @property
    def url(self) -> str:
        return f"sqlite:///{self.path.resolve()}"
