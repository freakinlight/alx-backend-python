#!/usr/bin/env python3
"""
This module defines a function that spawns task_wait_random n times and
returns a list of delays in ascending order.
"""
import asyncio
from typing import List
from tasks import task_wait_random  # Import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with max_delay and return
    a list of delays in ascending order without using sort().
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task  # Wait for the next task to finish
        # Insert delay in the correct position to maintain ascending order
        inserted = False
        for i in range(len(delays)):
            if delay < delays[i]:
                delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            delays.append(delay)
    return delays
