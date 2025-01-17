# merged types from pylance

from typing import Optional

from pandas._typing import Dtype as Dtype, Scalar
from pandas.core.dtypes.base import ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.cast import astype_nansafe as astype_nansafe
from pandas.core.dtypes.common import (
    is_bool_dtype as is_bool_dtype,
    is_object_dtype as is_object_dtype,
    is_scalar as is_scalar,
    is_string_dtype as is_string_dtype,
    pandas_dtype as pandas_dtype,
)
from pandas.core.dtypes.dtypes import (
    register_extension_dtype as register_extension_dtype,
)
from pandas.core.dtypes.missing import (
    isna as isna,
    na_value_for_dtype as na_value_for_dtype,
)

class SparseDtype(ExtensionDtype):
    def __init__(
        self, dtype: Dtype = ..., fill_value: Optional[Scalar] = ...
    ) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other) -> bool: ...
    @property
    def fill_value(self): ...
    @property
    def kind(self): ...
    @property
    def type(self): ...
    @property
    def subtype(self): ...
    @property
    def name(self): ...
    @classmethod
    def construct_array_type(cls): ...
    @classmethod
    def construct_from_string(cls, string): ...
    @classmethod
    def is_dtype(cls, dtype): ...
    def update_dtype(self, dtype): ...
