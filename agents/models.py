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
    description: str = Field(..., description="An atomic, independently assessable requirement.")
    category: JobRequirementCategories = Field(..., description="The semantic category of the requirement.")
    priority: JobRequirementPriorities = Field(..., description="Whether the requirement is required or preferred.")
    weight: float = Field(ge=0, le=100, description="Relative importance of this requirement as a percentage.")


class JobDescription(BaseModel):
    """ Job Description """
    position: str = Field(..., description="The position or title of the job.")
    organisation: str | None = Field(None, description="The name of the organisation offering the job.")
    department: str | None = Field(None, description="The department within the organisation.")
    requirements: list[JobRequirement] = Field(..., description="The list of job requirements.")


class Education(BaseModel):
    institution: str
    degree: str | None = None
    field_of_study: str | None = None
    graduation_date: str | None = None
    details: str | None = None


class Experience(BaseModel):
    position: str
    organisation: str | None = None
    location: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    highlights: list[str] = Field(default_factory=list)


class Project(BaseModel):
    name: str
    description: str | None = None
    technologies: list[str] = Field(default_factory=list)
    highlights: list[str] = Field(default_factory=list)


class CurriculumVitae(BaseModel):
    summary: str | None = None
    education: list[Education] = Field(default_factory=list)
    experience: list[Experience] = Field(default_factory=list)
    certifications: list[str] = Field(default_factory=list)
    skills: list[str] = Field(default_factory=list)
    projects: list[Project] = Field(default_factory=list)
