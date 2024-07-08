#!/usr/bin/env python3
"""async basics"""
import random
import asyncio


async def wait_random(max_delay: int = 0) -> float:
    """
    an asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random that waits for
    a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it
    """
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
