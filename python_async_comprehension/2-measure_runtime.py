#!/usr/bin/env python3
"""measure runtime of async_comprehension""""
import asyncio
from importlib import import_module as using
import time

async_comprehension = using('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """Measure the runtime of async_comprehension"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
