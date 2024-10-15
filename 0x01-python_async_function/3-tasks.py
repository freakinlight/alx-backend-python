#!/usr/bin/env python3
"""
This module defines a function that returns an asyncio.Task from wait_random.
"""
import asyncio
from basic_async_syntax import wait_random  # Import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
