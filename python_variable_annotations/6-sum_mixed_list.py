#!/usr/bin/env python3
"""function sum_mixed_list which takes a list mxd_lst"""

from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of the elements in the list"""
    return sum(mxd_lst)
