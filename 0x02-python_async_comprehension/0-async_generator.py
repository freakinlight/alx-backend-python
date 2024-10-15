#!/usr/bin/env python3
"""
This module demonstrates how to create an asynchronous generator in Python
using asyncio and random modules. It defines a coroutine that asynchronously
generates ten random floating-point numbers between 0 and 10, each after a
one-second delay.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """
    Asynchronously generate random numbers between 0 and 10.

    Repeatedly waits one second before yielding a random float within the
    specified range. This process is repeated ten times, demonstrating
    the use of 'await' within a generator to implement delays.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
