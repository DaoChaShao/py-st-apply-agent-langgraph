#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/10 17:52
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   types.py
# @Desc     :

from enum import StrEnum, unique


@unique
class JobRequirementCategories(StrEnum):
    EDUCATION = "education"
    EXPERIENCE = "experience"
    SKILLS = "skills"
    QUALIFICATIONS = "qualifications"
    CERTIFICATIONS = "certifications"
    RESPONSIBILITIES = "responsibilities"


@unique
class JobRequirementPriorities(StrEnum):
    REQUIRED = "required"
    PREFERRED = "preferred"
    UNSPECIFIED = "unspecified"


@unique
class ModelCategories(StrEnum):
    DEEPSEEK = "deepseek"
    OPENAI = "openai"


@unique
class ModelOutputMethods(StrEnum):
    FUNCTION_CALLING = "function_calling"
    JSON_MODE = "json_mode"
    JSON_SCHEMA = "json_schema"


@unique
class ResumeCategories(StrEnum):
    ADMINISTRATION = "administration"
    COMPUTER_SCIENCE = "computer_science"
    EDUCATION_TRAINING = "education_training"
    MANAGEMENT = "management"
    SPORTS = "sports"


@unique
class ParserCategories(StrEnum):
    CURRICULUM_VITAE = "cv"
    JOB_DESCRIPTION = "jd"


@unique
class ResumeComponents(StrEnum):
    SUMMARY = "summary"
    EDUCATION = "education"
    EXPERIENCE = "experience"
    SKILLS = "skills"
    QUALIFICATION = "qualification"
    CERTIFICATIONS = "certifications"
    PUBLICATIONS = "publications"
    AWARDS = "awards"
    PROJECTS = "projects"
    VOLUNTEERING = "volunteering"
