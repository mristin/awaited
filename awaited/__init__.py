"""Operate on awaitables and collections of awaitables."""
from typing import TypeVar, Callable, Awaitable, Iterable, AsyncIterable

U = TypeVar('U')
V = TypeVar('V')


async def then(awaitable: Awaitable[U], func: Callable[[U], V]) -> V:
    """Await the ``awaitable`` and then apply ``func`` on it."""
    return func(await awaitable)


async def these(awaitables: Iterable[Awaitable[U]]) -> AsyncIterable[U]:
    for awaitable in awaitables:
        yield await awaitable
