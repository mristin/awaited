"""Operate on awaitables and collections of awaitables."""
from typing import TypeVar, Callable, Awaitable, Iterable, AsyncIterable

U = TypeVar('U')
V = TypeVar('V')


async def that(func: Callable[[U], V], awaitable: Awaitable[U]) -> V:
    """Await the ``awaitable`` and then apply ``func`` on it."""
    return func(await awaitable)


async def these(
        func: Callable[[AsyncIterable[U]], Awaitable[V]],
        awaitables: Iterable[Awaitable[U]]
) -> V:
    """Map items of ``awaitables`` by awaiting and apply ``func`` on the mapping."""
    if isinstance(awaitables, AsyncIterable):
        raise ValueError(
            f"Unexpected async iterable: {awaitables}. "
            f"You probably want to use asyncstdlib for this case?")

    iterable_of_awaited = (await awaitable for awaitable in awaitables)

    assert isinstance(iterable_of_awaited, AsyncIterable)

    return await func(iterable_of_awaited)
