#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/5 22:17
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   models.py
# @Desc     :

from datetime import datetime
from typing import Annotated

from sqlalchemy import DateTime, Float, Integer, String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from .base import DECLARATION


class GEN:
    PK = Annotated[int, mapped_column(Integer, nullable=False, primary_key=True)]
    CT = Annotated[datetime, mapped_column(DateTime, nullable=False, server_default=func.now())]
    UT = Annotated[datetime, mapped_column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())]
    STR = Annotated[str, mapped_column(String(100), nullable=True)]
    NUM = Annotated[float, mapped_column(Float, nullable=True)]
    TXT = Annotated[str, mapped_column(Text, nullable=True)]


class ResumeEducation(DECLARATION):
    """ Resume Education Association Model """
    __tablename__ = "resume_education"

    resume_id: Mapped[int] = mapped_column(ForeignKey("resume.id"), primary_key=True)
    education_id: Mapped[int] = mapped_column(ForeignKey("education.id"), primary_key=True)


class Education(DECLARATION):
    """ Education Model """
    __tablename__ = "education"

    id: Mapped[GEN.PK]

    institution: Mapped[GEN.STR]
    degree: Mapped[GEN.STR]
    field_of_study: Mapped[GEN.STR]
    graduation_date: Mapped[GEN.STR]

    create_date: Mapped[GEN.CT]
    update_date: Mapped[GEN.UT]

    # Explicit Display
    resume: Mapped[list["Resume"]] = relationship(
        lazy="selectin",
        back_populates="education",
        secondary="resume_education",
    )

    def __repr__(self) -> str:
        """ Return a string representation of the Education object """
        return (
            f"<Education("
            f"id={self.id}, "
            f"institution={self.institution}, "
            f"degree={self.degree}, "
            f"field_of_study={self.field_of_study}, "
            f"graduation_date={self.graduation_date}, "
            f"create_date={self.create_date},"
            f"update_date={self.update_date}>"
        )


class Resume(DECLARATION):
    """ Resume Model """
    __tablename__ = "resume"

    id: Mapped[GEN.PK]

    category: Mapped[GEN.STR]
    summary: Mapped[GEN.TXT]

    create_date: Mapped[GEN.CT]
    update_date: Mapped[GEN.UT]

    # Explicit Display
    education: Mapped[list["Education"]] = relationship(
        lazy="selectin",
        back_populates="resume",
        secondary="resume_education",
    )

    def __repr__(self) -> str:
        """ Return a string representation of the Exercise object """
        return (
            f"<Resume("
            f"id={self.id}, "
            f"category={self.category}, "
            f"summary={self.summary}, "
            f"create_date={self.create_date},"
            f"update_date={self.update_date}>"
        )
