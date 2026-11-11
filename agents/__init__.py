#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/10 17:51
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   __init__.py.py
# @Desc     :

"""
****************************************************************
Agent - AI-Powered Application Toolkit
----------------------------------------------------------------
This module provides a unified interface for building and
managing AI-powered agents, including core services, data
models, and configuration enumerations.
****************************************************************
"""

__author__ = "Shawn Yu"
__version__ = "0.1.0"

from .services import (
    EmploymentDocParser,
    init_deepseek,
    init_openai,
    load_yaml,
)
from .types import (
    JobRequirementCategories,
    JobRequirementPriorities,
    ModelCategories,
    ModelOutputMethods,
    ParserCategories,
    ResumeCategories,
    ResumeComponents,
)

__all__ = [
    "EmploymentDocParser",
    "init_deepseek",
    "init_openai",
    "load_yaml",

    "JobRequirementCategories",
    "JobRequirementPriorities",
    "ModelOutputMethods",
    "ModelCategories",
    "ParserCategories",
    "ResumeCategories",
    "ResumeComponents",
]
