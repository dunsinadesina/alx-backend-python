#!/usr/bin/env python3
"""a function a variable to a kv pair"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """converts a python variable to a kv pair"""
    return k, v ** 2
