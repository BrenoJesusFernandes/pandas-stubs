from datetime import tzinfo as tzinfo
from typing import Optional, Union, overload

import numpy as np
from pandas._typing import Timedelta as Timedelta, Timestamp as Timestamp
from pandas.core.indexes.datetimelike import (
    DatetimelikeDelegateMixin as DatetimelikeDelegateMixin,
    DatetimeTimedeltaMixin as DatetimeTimedeltaMixin,
)
from pandas.core.indexes.timedeltas import TimedeltaIndex as TimedeltaIndex
from pandas.core.series import Series as Series, TimedeltaSeries, TimestampSeries

class DatetimeDelegateMixin(DatetimelikeDelegateMixin): ...

class DatetimeIndex(DatetimeTimedeltaMixin, DatetimeDelegateMixin):
    tz: Optional[tzinfo]
    def __init__(
        self,
        data=...,
        freq=...,
        tz=...,
        normalize: bool = ...,
        closed=...,
        ambiguous: str = ...,
        dayfirst: bool = ...,
        yearfirst: bool = ...,
        dtype=...,
        copy: bool = ...,
        name=...,
    ): ...
    def __array__(self, dtype=...) -> np.ndarray: ...
    def __reduce__(self): ...
    @overload
    def __add__(self, other: TimedeltaSeries) -> TimestampSeries: ...
    @overload
    def __add__(self, other: Union[Timedelta, TimedeltaIndex]) -> DatetimeIndex: ...
    def union_many(self, others): ...
    def to_series(self, keep_tz=..., index=..., name=...): ...
    def snap(self, freq: str = ...): ...
    def get_value(self, series, key): ...
    def get_value_maybe_box(self, series, key): ...
    def get_loc(self, key, method=..., tolerance=...): ...
    def slice_indexer(self, start=..., end=..., step=..., kind=...): ...
    def searchsorted(self, value, side: str = ..., sorter=...): ...
    def is_type_compatible(self, typ) -> bool: ...
    @property
    def inferred_type(self) -> str: ...
    def insert(self, loc, item): ...
    def indexer_at_time(self, time, asof: bool = ...): ...
    def indexer_between_time(
        self, start_time, end_time, include_start: bool = ..., include_end: bool = ...
    ): ...
    def strftime(self, date_format: str = ...) -> np.ndarray: ...

def date_range(
    start=...,
    end=...,
    periods=...,
    freq=...,
    tz=...,
    normalize=...,
    name=...,
    closed=...,
    **kwargs,
) -> DatetimeIndex: ...
def bdate_range(
    start=...,
    end=...,
    periods=...,
    freq: str = ...,
    tz=...,
    normalize: bool = ...,
    name=...,
    weekmask=...,
    holidays=...,
    closed=...,
) -> DatetimeIndex: ...
