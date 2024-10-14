#!/usr/bin/env python3
"""
This module measures the runtime of wait_n and returns
the average time per coroutine.
"""
import time
import asyncio
from typing import List
from concurrent_coroutines import wait_n  # Importing wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return the average time per coroutine.
    """
    start_time = time.perf_counter()  # Start the timer
    asyncio.run(wait_n(n, max_delay))  # Execute wait_n
    end_time = time.perf_counter()  # End the timer
    total_time = end_time - start_time  # Calculate total elapsed time
    return total_time / n  # Return average time per coroutine
