from typing import (
    List,
    Optional,
    Type,
)

from pandas._typing import ExtensionArray

class ExtensionDtype:
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other) -> bool: ...
    @property
    def na_value(self): ...
    @property
    def type(self) -> Type: ...
    @property
    def kind(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def names(self) -> Optional[List[str]]: ...
    @classmethod
    def construct_array_type(cls) -> Type[ExtensionArray]: ...
    @classmethod
    def construct_from_string(cls, string: str): ...
    @classmethod
    def is_dtype(cls, dtype) -> bool: ...
