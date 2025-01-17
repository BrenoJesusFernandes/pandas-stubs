from typing import Union

import numpy as np
from pandas.core.dtypes.generic import (
    ABCExtensionArray as ABCExtensionArray,
    ABCSeries as ABCSeries,
)

def should_extension_dispatch(left: ABCSeries, right) -> bool: ...
def should_series_dispatch(left, right, op): ...
def dispatch_to_extension_op(op, left: Union[ABCExtensionArray, np.ndarray], right): ...
