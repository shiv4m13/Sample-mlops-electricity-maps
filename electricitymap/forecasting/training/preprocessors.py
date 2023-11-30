from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

import pandas as pd
from sklearn.preprocessing import StandardScaler


class FeaturesPreprocessor(ABC):
    @abstractmethod
    def transform(self, X: pd.DataFrame, y: Optional[pd.DataFrame] = None):
        raise NotImplementedError

    @abstractmethod
    def update_valid_index(self, X: pd.DataFrame, only_on: Optional[List[str]] = None):
        raise NotImplementedError


class LassoPreprocessor(FeaturesPreprocessor):
    def __init__(
        self,
        scaler: StandardScaler,
        valid_index: pd.MultiIndex,
        feature_names: List[str],
    ) -> None:
        self.scaler = scaler
        self.valid_index = valid_index
        self.feature_names = feature_names

    def transform(
        self, X: pd.DataFrame, y: Optional[pd.DataFrame] = None
    ) -> Tuple[pd.DataFrame, Optional[pd.DataFrame]]:
        X = X.copy()
        X = X[self.feature_names]
        # apply valid index
        # print(self.valid_index)
        # X = X.loc[X.index.intersection(self.valid_index)]
        _X = self.scaler.transform(X)
        if y is not None:
            y = y.copy()
            y = y.loc[y.index.intersection(self.valid_index)]
        return pd.DataFrame(_X, index=X.index, columns=X.columns), y

    def update_valid_index(
        self, X: pd.DataFrame, only_on: Optional[List[str]] = None
    ) -> None:
        """Computes a new valid index for updated values
        as this valid index was computed during training
        time.
        """
        feature_names = self.feature_names
        if only_on is not None:
            assert all(
                [f in feature_names for f in only_on]
            ), f"Unknown feature name provided to update index, {[f for f in only_on if f not in feature_names]}"
            feature_names = only_on

        X = X.copy()
        X = X[feature_names]

        X = X[~X.isna().any(axis=1)]

        self.valid_index = X.index
