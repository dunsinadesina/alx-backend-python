#!/usr/bin/env python3
"""
    Import wait_random from the previous python file
    that you’ve written and write an async routine called wait_n
    that takes in 2 int arguments (in this order): n and max_delay
    You will spawn wait_random n times with the specified max_delay
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """executing multiple coroutimes at the same time"""
    delays: List[float] = []
    all_delays: List[float] = []
    for i in range(n):
        delays.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        all_delays.append(earliest_result)
    return all_delays
