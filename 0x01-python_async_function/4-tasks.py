#!/usr/bin/env python3
"""
Module that executes multiple coroutines concurrently using asyncio.
Each coroutine waits for a random delay and returns the delay time.
This module includes a function that spawns multiple tasks and returns
a list of delay times in ascending order.
"""
from typing import List
import asyncio
task_wait_random = __import__('tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns a list of all delay times (float values).
    The list is returned in ascending order.
    """
    futures = [task_wait_random(max_delay) for _ in range(n)]
    futures = asyncio.as_completed(futures)
    delays = [await future for future in futures]
    return sorted(delays)
