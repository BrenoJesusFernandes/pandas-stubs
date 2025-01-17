from typing import Any, Callable, Dict, Optional, Tuple

from pandas._typing import Scalar as Scalar

def make_rolling_apply(
    func: Callable[..., Scalar],
    args: Tuple,
    nogil: bool,
    parallel: bool,
    nopython: bool,
): ...
def generate_numba_apply_func(
    args: Tuple,
    kwargs: Dict[str, Any],
    func: Callable[..., Scalar],
    engine_kwargs: Optional[Dict[str, bool]],
): ...
