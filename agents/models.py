#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/10 18:17
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   models.py
# @Desc     :

from pydantic import BaseModel, Field

from .types import (
    JobRequirementCategories,
    JobRequirementPriorities,
)


class JobRequirement(BaseModel):
    """ Job Requirement """
    description: str
    category: JobRequirementCategories
    priority: JobRequirementPriorities
    weight: float = Field(ge=0, le=100)


class JobDescription(BaseModel):
    """ Job Description """
    position: str
    organisation: str | None = None
    department: str | None = None
    requirements: list[JobRequirement]
