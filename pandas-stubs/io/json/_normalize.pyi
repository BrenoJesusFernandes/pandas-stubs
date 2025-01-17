from typing import Any, Dict, List, Optional, Union

from pandas._typing import Scalar as Scalar
from pandas.core.frame import DataFrame as DataFrame

def convert_to_line_delimits(s: Any): ...
def nested_to_record(
    ds: Any,
    prefix: str = ...,
    sep: str = ...,
    level: int = ...,
    max_level: Optional[int] = ...,
) -> Any: ...
def json_normalize(
    data: Union[Dict, List[Dict]],
    record_path: Optional[Union[str, List]] = None,
    meta: Optional[Union[str, List[Union[str, List[str]]]]] = None,
    meta_prefix: Optional[str] = None,
    record_prefix: Optional[str] = None,
    errors: str = "raise",
    sep: str = ".",
    max_level: Optional[int] = None,
) -> DataFrame: ...
