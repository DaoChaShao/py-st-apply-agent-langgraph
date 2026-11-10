#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/10/21 19:42
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   preprocessor.py
# @Desc     :

from pathlib import Path
from typing import Any, Literal, Self

from access_modifiers import protectedmethod
from pandas import DataFrame, Series, read_csv, read_excel

from ..decorator import timer
from ..helper import Access
from ..highlighter import lines
from .types import (
    CategoricalImputationMethods,
    FeatureScalers,
    NumericImputationMethods,
    TabularFormats,
)


class DataImputer(Access):
    """ A class for imputing missing values in a dataset. """

    def __init__(
            self,
            data: DataFrame,
            *,
            cat_imputation_method: str | CategoricalImputationMethods | Literal[
                "mode", "constant", "ffill", "bfill"
            ] = "mode",
            num_imputation_method: str | NumericImputationMethods | Literal[
                "linear", "mean", "median", "zero", "ffill", "bfill"
            ] = "linear",
            constant_value: Any = "Unknown",
    ) -> None:
        """
        Initialise the DataImputer class

        :param data: The dataset to be imputed.
        :param cat_imputation_method: The method to be used for imputing categorical data.
        :param num_imputation_method: The method to be used for imputing numeric data.
        :param constant_value: The value to be used for imputing missing values in categorical data.
        :return: None
        """
        super().__init__()
        self._data: DataFrame = data
        self._cat_method: CategoricalImputationMethods = CategoricalImputationMethods(cat_imputation_method)
        self._num_method: NumericImputationMethods = NumericImputationMethods(num_imputation_method)
        self._constant_val: Any = constant_value

    def _divide(self) -> tuple[DataFrame, DataFrame]:
        """ Divide the data into numeric and categorical columns based on the specified category """
        _num_data = self._data.select_dtypes(include=["number"])
        _cat_data = self._data.select_dtypes(include=["object", "category", "string"])
        return _num_data, _cat_data

    def _impute_numeric_data(self, data: DataFrame) -> DataFrame:
        """ Impute missing values in the numeric data based on the specified method """
        match self._num_method:
            case NumericImputationMethods.LINEAR:
                return data.interpolate(method="linear", limit_direction="both")
            case NumericImputationMethods.MEAN:
                return data.fillna(data.mean())
            case NumericImputationMethods.MEDIAN:
                return data.fillna(data.median())
            case NumericImputationMethods.ZERO:
                return data.fillna(0)
            case NumericImputationMethods.FORWARD_FILL:
                return data.ffill()
            case NumericImputationMethods.BACKWARD_FILL:
                return data.bfill()
        raise ValueError(f"Unsupported numeric method: {self._num_method}")

    def _impute_categorical(self, data: DataFrame) -> DataFrame:
        """ Impute missing values in the categorical data based on the specified method """
        match self._cat_method:
            case CategoricalImputationMethods.MODE:
                modes = data.mode(dropna=True)
                return data.fillna(modes.iloc[0]) if not modes.empty else data
            case CategoricalImputationMethods.CONSTANT:
                return data.fillna(self._constant_val)
            case CategoricalImputationMethods.FORWARD_FILL:
                return data.ffill()
            case CategoricalImputationMethods.BACKWARD_FILL:
                return data.bfill()
        raise ValueError(f"Unsupported categorical method: {self._cat_method}")

    def impute(self) -> DataFrame:
        """ Impute missing values in the data based on the specified category and method """
        _num_data, _cat_data = self._divide()
        self._data[_num_data.columns] = self._impute_numeric_data(_num_data)
        self._data[_cat_data.columns] = self._impute_categorical(_cat_data)
        return self._data

    def __enter__(self) -> Self:
        """ Enter the context manager """
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """ Exit the context manager """
        pass


class FeatureScaler(Access):
    """ A class for scaling features in a dataset """

    def __init__(
            self,
            features: DataFrame,
            *,
            category: str | FeatureScalers | Literal[
                "normalisation", "standardisation", "robustification"
            ] = "normalisation",
            min_scaler: float = 0.0,
            max_scaler: float = 1.0,
    ) -> None:
        """
        Initialise the FeatureScaler class

        :param features: The features to be scaled.
        :param category: The category of scaling to be applied.
        :param min_scaler: The minimum value for scaling.
        :param max_scaler: The maximum value for scaling.
        :return: None
        """
        super().__init__()
        self._features: DataFrame = features
        self._category: str = FeatureScalers(category)
        self._min: float = min_scaler
        self._max: float = max_scaler

        if min_scaler >= max_scaler:
            raise ValueError("min_scaler must be less than max_scaler")

    def _normalisation(self) -> DataFrame:
        """ Normalise the features using min-max scaling """
        _min_vals = self._features.min()
        _ranges = self._features.max() - _min_vals
        _scaled = (self._features - _min_vals) / _ranges.replace(0, 1)
        return _scaled * (self._max - self._min) + self._min

    def _standardisation(self) -> DataFrame:
        """ Standardise the features using z-score normalisation """
        _mean = self._features.mean()
        _std = self._features.std(ddof=0)
        return (self._features - _mean) / _std.replace(0, 1)

    def _robustification(self) -> DataFrame:
        """ Robustify the features using IQR scaling """
        _median = self._features.median()
        _iqr = self._features.quantile(0.75) - self._features.quantile(0.25)
        return (self._features - _median) / _iqr.replace(0, 1)

    def scale(self) -> DataFrame:
        """ Scale the features based on the specified category """
        match self._category:
            case FeatureScalers.NORMALISATION:
                return self._normalisation()
            case FeatureScalers.STANDARDISATION:
                return self._standardisation()
            case FeatureScalers.ROBUSTIFICATION:
                return self._robustification()
            case _:
                raise ValueError(f"Unsupported category: {self._category}")

    def __enter__(self) -> Self:
        """ Enter the context manager. """
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """ Exit the context manager. """
        pass

    def __repr__(self) -> str:
        """ Return the string representation of the FeatureSelector class. """
        return (
            f"FeatureSelector("
            f"features={self._features!r}, "
            f"category={self._category!r}, "
            f"min_scaler={self._min!r}, "
            f"max_scaler={self._max!r})"
        )


class TabularLoader(Access):
    """ Load and display data from a file. """

    def __init__(self, filepath: str | Path, *, display: bool = True) -> None:
        """
        Initialise the FileLoader class

        :param filepath: The path to the file.
        :param display: Whether to display the dataset content and summary.
        :return: None
        """
        super().__init__()
        self._path: Path = Path(filepath)
        self._type: TabularFormats | None = None
        self._display: bool = display
        self._dataset: DataFrame | None = None

    def load(self, file_category: str | TabularFormats | Literal["csv", "excel"] = TabularFormats.CSV) -> DataFrame:
        """
        Load data from a file based on the specified file category.

        :param file_category: The category of the file (csv or excel).
        :return: The loaded dataset.
        """
        self._type: TabularFormats = TabularFormats(file_category)
        match self._type:
            case TabularFormats.CSV:
                self._dataset = read_csv(self._path.resolve())
            case TabularFormats.EXCEL:
                self._dataset = read_excel(self._path.resolve())
            case _:
                raise ValueError(f"Invalid file category: {self._type}")

        if self._display:
            self._display_info()
        return self._dataset

    def __enter__(self) -> Self:
        """ Enter the context manager. """
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """
        Exit the context manager.

        :param exc_type: The type of exception that occurred.
        :param exc_value: The exception that occurred.
        :param traceback: The traceback of the exception.
        :return: None
        """
        pass

    @protectedmethod
    def _display_info(self) -> None:
        """ Display information: head, description, duplicated rows, missing values and missing values details. """
        if self._dataset is None:
            return

        print(self._dataset.head())
        print()
        print(self._dataset.describe())
        print()
        _dup_rows: float = self._dataset.duplicated().sum()
        _miss_values: float = self._dataset.isnull().sum().sum()
        _miss_details: Series = self._dataset.isnull().sum()[self._dataset.isnull().sum() > 0]
        print(f"Duplicated Rows: {_dup_rows}")
        print(f"Missing Values: {_miss_values}")
        if not _miss_details.empty:
            print(f"Missing Values Details:\n{_miss_details}")
        else:
            print("Missing Values Details: None")

    @property
    def dataset(self) -> DataFrame | None:
        """ Return the dataset """
        return self._dataset

    def __len__(self) -> int:
        """ Return the length of the dataset. """
        return len(self._dataset) if self._dataset is not None else 0

    def __repr__(self) -> str:
        """ Return the string representation of the FileLoader class. """
        return (
            f"TabularLoader("
            f"filepath={self._path!r}, "
            f"file_category={self._type!r}, "
            f"display={self._display!r})"
        )


@timer
def get_cls_label_distribution(
        labels: Series,
        *,
        threshold: float = 1.5,
        display: bool = False
) -> tuple[Series, Series, float, bool, int]:
    """
    Check the distribution of the labels in the target variable and evaluate class balance.

    :param labels: The target label series.
    :param threshold: The Imbalance Ratio (IR) threshold to judge imbalance (default: 1.5).
    :param display: Whether to display formatted label counts, proportions, and balance verdict.
    :return: Tuple of (counts, proportions, imbalance_ratio, is_balanced)
    """
    _counts: Series = labels.value_counts()
    _proportions: Series = labels.value_counts(normalize=True)

    # Calculate Imbalance Rate (Max Count / Min Count)
    _max_count = int(_counts.max())
    _min_count = int(_counts.min()) if _counts.min() > 0 else 1
    ir: float = round(_max_count / _min_count, 2)

    # Determine if the class balance is acceptable
    _is_balanced: bool = ir < threshold

    # Determine the number of classes
    _n_classes: int = _counts.size

    # Display the label counts, proportions, and balance verdict
    if display:
        print(_counts)
        lines()
        print(_proportions)
        lines()
        print(f"Max Count / Min Count : {_max_count} / {_min_count}")
        print(f"Imbalance Ratio (IR)  : {ir:.2f}")

        # Provide an intuitive conclusion
        if ir < 1.5:
            verdict = "Balanced (Sample distribution is very balanced)"
        elif 1.5 <= ir < 3.0:
            verdict = "Mildly Imbalanced (Mild imbalance)"
        elif 3.0 <= ir < 5.0:
            verdict = "Moderately Imbalanced (Moderate imbalance, pay attention)"
        else:
            verdict = "Severely Imbalanced (Severe imbalance, resampling or weight setting required)"
        print(f"Status                : {verdict}")
        lines()
        print(f"Number of classes     : {_n_classes}")
    return _counts, _proportions, ir, _is_balanced, _n_classes


@timer
def get_reg_label_distribution(labels: Series, *, display: bool = True) -> dict:
    """
    Analyse the distribution features of continuous regression targets

    :param labels: the target variable
    :param display: Toggle for printing the distribution summary
    :return: the distribution summary
    """
    _stats: dict[str, float] = {
        "count": len(labels),
        "mean": labels.mean(),
        "std": labels.std(),
        "min": labels.min(),
        "25%": labels.quantile(0.25),
        "median": labels.median(),
        "75%": labels.quantile(0.75),
        "max": labels.max(),
        "skewness": labels.skew(),
        "kurtosis": labels.kurt(),
    }

    if display:
        for key, value in _stats.items():
            print(f"{key:<10}: {value:.4f}")
        lines()

        # Bias Situations
        if _stats["skewness"] > 1.0:
            print("Status: Highly Right-Skewed (Strongly recommend log1p transformation)")
        elif 0.5 < _stats["skewness"] <= 1.0:
            print("Status: Moderately Right-Skewed (Consider log1p transformation)")
        elif -1.0 <= _stats["skewness"] < -0.5:
            print("Status: Moderately Left-Skewed")
        elif _stats["skewness"] < -1.0:
            print("Status: Highly Left-Skewed")
        else:
            print("Status: Fairly Symmetric Distribution")
    return _stats
