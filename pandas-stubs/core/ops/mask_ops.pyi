from typing import Optional, Union

import numpy as np
from pandas._libs import missing as libmissing

def kleene_or(
    left: Union[bool, np.ndarray],
    right: Union[bool, np.ndarray],
    left_mask: Optional[np.ndarray],
    right_mask: Optional[np.ndarray],
): ...
def kleene_xor(
    left: Union[bool, np.ndarray],
    right: Union[bool, np.ndarray],
    left_mask: Optional[np.ndarray],
    right_mask: Optional[np.ndarray],
): ...
def kleene_and(
    left: Union[bool, libmissing.NAType, np.ndarray],
    right: Union[bool, libmissing.NAType, np.ndarray],
    left_mask: Optional[np.ndarray],
    right_mask: Optional[np.ndarray],
): ...
def raise_for_nan(value, method) -> None: ...
