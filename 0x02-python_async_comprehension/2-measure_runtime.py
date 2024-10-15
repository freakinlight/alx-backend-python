#!/usr/bin/env python3
"""
Module to measure runtime of async comprehensions executed in parallel.
"""

import asyncio
import time
from async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of executing async_comprehension four times
    concurrently.
    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start_time


async def main():
    """
    Main coroutine that prints the measured runtime.
    """
    runtime = await measure_runtime()
    print(runtime)

if __name__ == '__main__':
    asyncio.run(main())
