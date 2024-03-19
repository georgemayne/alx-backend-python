#!/usr/bin/env python3
""" 10 random numbers using an async comprehensing over """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous coroutine that uses async comprehension to
    collect 10 random numbers from the async_generator
    and returns them as a list.
    """
    rslt = [i async for i in async_generator()]
    return rslt
