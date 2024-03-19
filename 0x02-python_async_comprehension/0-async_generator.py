#!/usr/bin/env python3
""" async_generator that takes no arguments """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields 10 random numbers between 0 and 10,
    pausing for 1 second between each yield.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
