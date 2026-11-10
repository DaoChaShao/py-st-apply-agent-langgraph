#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/10/21 19:45
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   types.py
# @Desc     :

from enum import StrEnum, unique


@unique
class FeatureScalers(StrEnum):
    NORMALISER = "normaliser"
    STANDARDISER = "standardiser"
    ROBUST_SCALER = "robust_scaler"


@unique
class Languages(StrEnum):
    """ Programming languages. """
    CN = "Chinese"
    EN = "English"


@unique
class Missions(StrEnum):
    """ Machine learning missions. """
    CLS = "cls"
    REG = "reg"



