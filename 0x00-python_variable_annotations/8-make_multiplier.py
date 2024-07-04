#!/usr/bin/env python3
"""function that multiplies a float by multiplier and return a function"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplies a float by a multiplier
    Args:
        multiplier(float): multiplier
    Returns:
        function that multiplies a float by multiplier
    """

    def multiplier_func(number: float) -> float:
        """multiplies a float by a multiplier"""
        return multiplier * number

    return multiplier_func
