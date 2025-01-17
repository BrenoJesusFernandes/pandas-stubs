from typing import Any, Callable, List, Mapping, Optional, Tuple, Type, TypeVar, Union

from pandas._libs.properties import cache_readonly as cache_readonly

FuncType = Callable[..., Any]
F = TypeVar("F", bound=FuncType)

def deprecate(
    name: str,
    alternative: Callable[..., Any],
    version: str,
    alt_name: Optional[str] = ...,
    klass: Optional[Type[Warning]] = ...,
    stacklevel: int = ...,
    msg: Optional[str] = ...,
) -> Callable[..., Any]: ...
def deprecate_kwarg(
    old_arg_name: str,
    new_arg_name: Optional[str],
    mapping: Optional[Union[Mapping[Any, Any], Callable[[Any], Any]]] = ...,
    stacklevel: int = ...,
) -> Callable[..., Any]: ...
def rewrite_axis_style_signature(
    name: str, extra_params: List[Tuple[str, Any]]
) -> Callable[..., Any]: ...

class Substitution:
    params = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __call__(self, func: F) -> F: ...
    def update(self, *args, **kwargs) -> None: ...

class Appender:
    addendum: Optional[str]
    join = ...
    def __init__(
        self, addendum: Optional[str], join: str = ..., indents: int = ...
    ) -> None: ...
    def __call__(self, func: F) -> F: ...

def indent(text: Optional[str], indents: int = ...) -> str: ...
