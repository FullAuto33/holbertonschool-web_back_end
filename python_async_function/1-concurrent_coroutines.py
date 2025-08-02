#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """return waitrandom n time"""
    coroutines = [wait_random(max_delay) for _ in range(n)]

    delays =[]
    for completed in asyncio.as_completed(coroutines):
        delay = await completed
        delays.append(delay)
    return delays
