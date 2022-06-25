from __future__ import annotations

from typing import Callable, Generic, List, Literal, Optional, Tuple, Union, overload

import numpy as np
from pandas._typing import (
    T1 as T1,
    DataFrame as DataFrame,
    Index as Index,
    Scalar,
    Series as Series,
    SeriesAxisType,
    np_ndarray_int64,
    np_ndarray_str,
)
from pandas.core.accessor import DirNamesMixin as DirNamesMixin
from pandas.core.arrays import ExtensionArray as ExtensionArray
from pandas.core.arrays.categorical import Categorical

class PandasObject(DirNamesMixin):
    def __sizeof__(self) -> int: ...

class NoNewAttributesMixin:
    def __setattr__(self, key, value) -> None: ...

class GroupByError(Exception): ...
class DataError(GroupByError): ...
class SpecificationError(GroupByError): ...

class SelectionMixin:
    def ndim(self) -> int: ...
    def __getitem__(self, key): ...
    def aggregate(
        self, func: Optional[Callable] = ..., *args, **kwargs
    ) -> Union[Scalar, Series, DataFrame]: ...
    agg = aggregate

class ShallowMixin: ...

class IndexOpsMixin:
    __array_priority__: int = ...
    def transpose(self, *args, **kwargs) -> IndexOpsMixin: ...
    @property
    def T(self) -> IndexOpsMixin: ...
    @property
    def shape(self) -> tuple: ...
    @property
    def ndim(self) -> int: ...
    def item(self): ...
    @property
    def nbytes(self) -> int: ...
    @property
    def size(self) -> int: ...
    @property
    def array(self) -> ExtensionArray: ...
    def to_numpy(self) -> np.ndarray: ...
    @property
    def empty(self) -> bool: ...
    def max(self, axis=..., skipna: bool = ..., **kwargs): ...
    def min(self, axis=..., skipna: bool = ..., **kwargs): ...
    def argmax(
        self, axis: Optional[SeriesAxisType] = ..., skipna: bool = ..., *args, **kwargs
    ) -> np.ndarray: ...
    def argmin(
        self, axis: Optional[SeriesAxisType] = ..., skipna: bool = ..., *args, **kwargs
    ) -> np.ndarray: ...
    def tolist(self) -> List: ...
    def to_list(self) -> List: ...
    def __iter__(self): ...
    def hasnans(self) -> bool: ...
    def value_counts(
        self,
        normalize: bool = ...,
        sort: bool = ...,
        ascending: bool = ...,
        bins=...,
        dropna: bool = ...,
    ): ...
    def nunique(self, dropna: bool = ...) -> int: ...
    @property
    def is_unique(self) -> bool: ...
    @property
    def is_monotonic(self) -> bool: ...
    @property
    def is_monotonic_decreasing(self) -> bool: ...
    @property
    def is_monotonic_increasing(self) -> bool: ...
    def factorize(
        self, sort: bool = ..., na_sentinel: int = ...
    ) -> Tuple[np.ndarray, Union[np.ndarray, Index, Categorical]]: ...
    def searchsorted(
        self, value, side: str = ..., sorter=...
    ) -> Union[int, List[int]]: ...
    def drop_duplicates(
        self, keep: Literal["first", "last", False] = ...
    ) -> IndexOpsMixin: ...
