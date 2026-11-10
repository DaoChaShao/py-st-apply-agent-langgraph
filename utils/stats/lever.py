#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/10/28 22:59
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   lever.py
# @Desc     :

from random import getstate, setstate
from random import seed as rnd_seed
from time import perf_counter
from typing import Self

from numpy import random as np_random
from pandas import DataFrame, option_context

from ..constants import WIDTH
from ..decorator import timer
from ..highlighter import lines


class NumpySeed:
    """ Setting numpy random seed for reproducibility """

    def __init__(self, description: str, seed: int = 27, tick_tock: bool = False) -> None:
        """
        Initialise the RandomSeed class

        :param description: the description of a random seed
        :param seed: the seed value to be set
        :param tick_tock: whether to measure elapsed time
        """
        self._description: str = description
        self._seed: int = seed
        self._previous_py_seed = None
        self._previous_np_seed = None

        self._tick: bool = tick_tock
        self._start: float = 0.0
        self._end: float = 0.0
        self._elapsed: float = 0.0

    def __enter__(self) -> Self:
        """ Set the random seed """
        if self._tick:
            self._start = perf_counter()

        # Save the previous random seed state
        self._previous_py_seed = getstate()
        self._previous_np_seed = np_random.get_state()

        # Set the new random seed
        rnd_seed(self._seed)
        np_random.seed(self._seed)

        print("*" * WIDTH)
        print(f"{self._description} has been set to {self._seed}.")
        print("-" * WIDTH)
        return self

    def __exit__(self, *args):
        """ Exit the random seed context manager """
        # Restore the previous random seed state
        if self._previous_py_seed is not None:
            setstate(self._previous_py_seed)
        if self._previous_np_seed is not None:
            np_random.set_state(self._previous_np_seed)

        # Calculate elapsed time if measuring
        if self._tick:
            self._end = perf_counter()
            self._elapsed = self._end - self._start

        print("-" * WIDTH)
        print(f"{self._description} has been restored to previous randomness.")
        if self._tick:
            elapsed_time: str = self._format_time(self._elapsed)
            print(f"{self._description} took {elapsed_time}.")
        print("*" * WIDTH)
        print()
        # Return False to propagate exceptions, True to suppress them
        return False

    @staticmethod
    def _format_time(seconds: float) -> str:
        """
        Format time breakdown from seconds to days, hours, minutes, and seconds

        :param seconds: time in seconds
        :return: formatted time breakdown string
        """
        if seconds < 1.0:
            return f"{seconds * 1000:.1f} ms"

        _days: int = int(seconds // 86400)
        _hours: int = int((seconds % 86400) // 3600)
        _minutes: int = int((seconds % 3600) // 60)
        _secs: float = seconds % 60

        _parts: list[str] = []
        if _days > 0:
            _parts.append(f"{_days} days")
        if _hours > 0:
            _parts.append(f"{_hours} hours")
        if _minutes > 0:
            _parts.append(f"{_minutes} minutes")
        if _secs > 0 or not _parts:
            _parts.append(f"{_secs:.2f} seconds")
        return " ".join(_parts)

    def __repr__(self) -> str:
        """ Return a string representation of the random seed """
        _base: str = f"NumpyRandomSeed(description={self._description}, seed={self._seed})"
        if self._tick and self._elapsed > 0:
            _base += f", Elapsed Time: {self._elapsed:.2f} s"
        return _base


@timer
def summary_dataframe(data: DataFrame, *, display: bool = True) -> None:
    """
    Print summary statistics of the data

    :param data: DataFrame containing the data
    :param display: Whether to print the summary in console.
    :return: None
    """
    with option_context(
            "display.max_columns", None,
            "display.width", 1_000,
            "display.max_colwidth", None
    ):
        if display:
            print(data.head())
            lines()
            print(f"Data Amount: {len(data)}.")
            lines()
            print(data.describe())
            lines()
            print(f"Missing Values:\n{data.isnull().sum()[data.isnull().sum() > 0]}")
            lines()
            print(f"Duplicated Rows: {data.duplicated().sum()}")
