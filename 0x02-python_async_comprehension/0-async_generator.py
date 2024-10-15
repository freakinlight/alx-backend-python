#!/usr/bin/env python3
"""
This module demonstrates the use of asynchronous generators
and async comprehensions in Python. It features a coroutine
that generates random floating numbers between 0 and 10 after a
set delay and another coroutine that consumes these numbers.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields a random floating number
    between 0 and 10 after waiting for one second. It loops ten times.

    Yields:
        float: A random number between 0 and 10 after each one-second delay.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def print_yielded_values() -> None:
    """
    Coroutine that consumes values from async_generator
    and prints them in a list.
    This demonstrates how to collect and utilize values
    from an asynchronous generator.

    Prints:
        list: A list of floating numbers generated by async_generator.
    """
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

if __name__ == '__main__':
    asyncio.run(print_yielded_values())
