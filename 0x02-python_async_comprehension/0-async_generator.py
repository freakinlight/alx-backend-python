#!/usr/bin/env python3
import asyncio
import random
"""
This module demonstrates async generators and comprehensions with asyncio
and random module, printing yielded random numbers.
"""


async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

if __name__ == '__main__':
    asyncio.run(print_yielded_values())
