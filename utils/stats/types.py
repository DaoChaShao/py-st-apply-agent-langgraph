#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/10/28 23:13
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   types.py
# @Desc     :

from enum import StrEnum, unique


@unique
class CategoricalImputationMethods(StrEnum):
    MODE = "mode"
    CONSTANT = "constant"
    FFILL = "ffill"
    BFILL = "bfill"


@unique
class FeatureScalers(StrEnum):
    NORMALISATION = "normalisation"
    STANDARDISATION = "standardisation"
    ROBUSTIFICATION = "robustification"


@unique
class NumericImputationMethods(StrEnum):
    LINEAR = "linear"
    MEAN = "mean"
    MEDIAN = "median"
    ZERO = "zero"
    FFILL = "ffill"
    BFFILL = "bfill"


@unique
class TabularFormats(StrEnum):
    CSV = "csv"
    EXCEL = "excel"
