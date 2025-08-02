#!/usr/bin/env python3
"""function make_multiplier that takes a float multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    def multiplier_function(value: float) -> float:
        """multiplies value by multiplier"""
        return value * multiplier

    return multiplier_function
