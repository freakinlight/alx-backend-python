#!/usr/bin/env python3
"""
This module demonstrates async generators and comprehensions with asyncio
and random module, printing yielded random numbers.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously yield random numbers between 0 and 10.
    Repeats 10 times with a 1-second delay each iteration. Each number yielded
    is a float.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def print_yielded_values() -> None:
    """
    Collect and print values from async_generator.
    Collects numbers into a list and prints them for testing.
    """
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)
