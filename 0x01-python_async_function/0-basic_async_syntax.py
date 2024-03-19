
#!/usr/bin/env python3
""" Asynchronous coroutine that waits for a random
delay between 0 and max_delay (inclusive).
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    delay between 0 and max_delay

    max_delay,with a default value of 10
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
