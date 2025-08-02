#!/usr/bin/env python3
"""function’s parameters and return values """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable) -> List[Tuple[int, int]]:
    """returns a list of tuples"""
    return [(i, len(x)) for i, x in enumerate(lst)]
