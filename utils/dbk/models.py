#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/5 22:17
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   models.py
# @Desc     :

from datetime import datetime
from datetime import time as date_time
from typing import Annotated

from sqlalchemy import DateTime, Float, Integer, String, Time
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from .base import DECLARATION


class GEN:
    PK = Annotated[int, mapped_column(Integer, nullable=False, primary_key=True)]
    CONTENT = Annotated[str, mapped_column(String(50), nullable=False)]
    CT = Annotated[datetime, mapped_column(DateTime, nullable=False, server_default=func.now())]
    UT = Annotated[datetime, mapped_column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())]


class Exercise(DECLARATION):
    """ Exercise Model """

    __tablename__ = "exercise"

    id: Mapped[GEN.PK]

    # Exercise Date and time
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    time: Mapped[date_time] = mapped_column(Time, nullable=False)
    week: Mapped[str] = mapped_column(String(10), nullable=False)
    type: Mapped[str] = mapped_column(String(10), nullable=False, default="J")

    # Exercise Index
    slope: Mapped[float] = mapped_column(Float, nullable=True)
    duration: Mapped[float] = mapped_column(Float, nullable=True)
    distance: Mapped[float] = mapped_column(Float, nullable=False, default=5.0)
    active_kilocalories: Mapped[float] = mapped_column(Float, nullable=True)
    total_kilocalories: Mapped[float] = mapped_column(Float, nullable=True)
    avg_cadence: Mapped[int] = mapped_column(Integer, nullable=True)
    avg_pace: Mapped[float] = mapped_column(Float, nullable=True)
    avg_heart_rate: Mapped[int] = mapped_column(Integer, nullable=True)
    effort: Mapped[int] = mapped_column(Integer, nullable=True)

    # Heart Rate Zones
    zone_i: Mapped[float] = mapped_column(Float, nullable=True)
    zone_ii: Mapped[float] = mapped_column(Float, nullable=True)
    zone_iii: Mapped[float] = mapped_column(Float, nullable=True)
    zone_iv: Mapped[float] = mapped_column(Float, nullable=True)
    zone_v: Mapped[float] = mapped_column(Float, nullable=True)

    # Heart Rate Recovery
    post_heart_rate_i: Mapped[int] = mapped_column(Integer, nullable=True)
    post_heart_rate_ii: Mapped[int] = mapped_column(Integer, nullable=True)
    post_heart_rate_iii: Mapped[int] = mapped_column(Integer, nullable=True)

    # Body Weight
    weight: Mapped[float] = mapped_column(Float, nullable=True)

    # ACWR (Acute-Chronic Workload Ratio) - RPE (Rate of Perceived Exertion): Training Intensity
    rpe: Mapped[int] = mapped_column(Integer, nullable=True)

    create_date: Mapped[GEN.CT]
    update_date: Mapped[GEN.UT]

    def __repr__(self) -> str:
        """ Return a string representation of the Exercise object """
        return (
            f"<Exercise("
            f"id={self.id}, "
            f"date={self.date}, time={self.time}, week={self.week}, "
            f"type={self.type}, "
            f"slope={self.slope}, duration={self.duration}, distance={self.distance}, "
            f"active_kilocalories={self.active_kilocalories}, total_kilocalories={self.total_kilocalories}, "
            f"avg_cadence={self.avg_cadence}, avg_pace={self.avg_pace}, avg_heart_rate={self.avg_heart_rate}, "
            f"effort={self.effort}, "
            f"zone_i={self.zone_i}, "
            f"zone_ii={self.zone_ii}, "
            f"zone_iii={self.zone_iii}, "
            f"zone_iv={self.zone_iv}, "
            f"zone_v={self.zone_v}, "
            f"post_heart_rate_i={self.post_heart_rate_i}, "
            f"post_heart_rate_ii={self.post_heart_rate_ii}, "
            f"post_heart_rate_iii={self.post_heart_rate_iii}, "
            f"weight={self.weight}, "
            f"create_date={self.create_date}, update_date={self.update_date}, "
            f"rpe={self.rpe}>"
        )
