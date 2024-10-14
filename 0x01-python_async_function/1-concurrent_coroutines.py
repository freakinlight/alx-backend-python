#!/usr/bin/env python3
"""
This module defines a coroutine that spawns multiple wait_random coroutines
and returns a list of delays in ascending order.
"""
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with max_delay and return a list of delays
    in ascending order without using sort().
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
