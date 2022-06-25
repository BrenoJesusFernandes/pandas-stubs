from typing import Type

from pandas.core.dtypes.base import ExtensionDtype as ExtensionDtype

from .masked import BaseMaskedArray as BaseMaskedArray

class _IntegerDtype(ExtensionDtype):
    name: str
    base = ...
    type: Type
    na_value = ...
    def is_signed_integer(self): ...
    def is_unsigned_integer(self): ...
    def numpy_dtype(self): ...
    def kind(self): ...
    def itemsize(self): ...
    @classmethod
    def construct_array_type(cls): ...
    def __from_arrow__(self, array): ...

def integer_array(values, dtype=..., copy: bool = ...): ...
def safe_cast(values, dtype, copy): ...
def coerce_to_array(values, dtype, mask=..., copy: bool = ...): ...

class IntegerArray(BaseMaskedArray):
    def dtype(self): ...
    def __init__(self, values, mask, copy: bool = ...) -> None: ...
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs): ...
    def __setitem__(self, key, value) -> None: ...
    def astype(self, dtype, copy: bool = ...): ...

class Int8Dtype: ...
class Int16Dtype: ...
class Int32Dtype: ...
class Int64Dtype: ...
class UInt8Dtype: ...
class UInt16Dtype: ...
class UInt32Dtype: ...
class UInt64Dtype: ...
