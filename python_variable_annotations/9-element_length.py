#!/usr/bin/env python3
"""function’s parameters and return values """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples"""
    return [(x, len(x)) for x in lst]
