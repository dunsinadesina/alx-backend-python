#!/usr/bin/env python3
"""a function that takes a mxed list of integers and floats and returns sum"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a mxed list of integers and floats and returns sum"""
    return sum(mxd_lst)
