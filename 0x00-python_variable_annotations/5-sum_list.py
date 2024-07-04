#!/usr/bin/env python3
"""a function that returns the sum of list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sums up a list of floats
    Args:
        input_list(list): list of floats
    Returns:
        float: sum of floats
    """
    if input_list is None:
        return 0
    else:
        return sum(input_list)
