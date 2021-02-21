from typing import List

import pytest
import asyncstdlib

import awaited


@pytest.mark.asyncio
async def test_then():
    async def async_func() -> List[int]:
        return [1, 2, 3]

    awaited_sum = await awaited.then(async_func(), sum)
    assert awaited_sum == 6


@pytest.mark.asyncio
async def test_these_on_sync_iterable():
    async def async_is_non_negative(x: int) -> bool:
        return x > 0

    result = await asyncstdlib.all(
        awaited.these(
            async_is_non_negative(x) for x in [1, 2, 3]))

    assert result


@pytest.mark.asyncio
async def test_that_these_is_unnecessary_on_async_iterable():
    async def async_is_non_negative(x: int) -> bool:
        return x > 0

    async def async_generator():
        for x in [10, 20, 30]:
            yield x

    result = await asyncstdlib.all(
        asyncstdlib.map(async_is_non_negative, async_generator()))

    assert result
