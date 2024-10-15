#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('async_comprehension').async_comprehension


async def main():
    print(await async_comprehension())

asyncio.run(main())

