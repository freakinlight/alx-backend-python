#!/usr/bin/env python3
"""
Module uses async comprehensions to collect values from an asynchronous
generator.
"""

import asyncio
from typing import List

# Adjust the import if necessary depending on your project structure
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from
    async_generator using async comprehension.
    Returns:
        List[float]: List of 10 random numbers.
    """
    return [i async for i in async_generator()]


async def main():
    """
    Main coroutine that invokes async_comprehension and prints its result.
    This function is the entry point of the program when executed.
    """
    print(await async_comprehension())

if __name__ == '__main__':
    asyncio.run(main())
