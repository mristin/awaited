*******
Awaited
*******

Awaited is a micro-library for operations on awaitables and collections of awaitables.

Goal
====
**Make up for lack of async lambdas**.
It is meant to make up for lack of async lambdas in Python (see Python `issue 33447`_).
While you might not use async lambdas often, they are important for use cases
where you need to specify chained operations.
Good naming of short lambda functions is hard as the name might be more complex than
the body of the lambda function itself.
In those cases, where the downstream code can deal with a lambda returning
a `coroutine`_, chaining operations using *awaited* library can be convenient.

.. _issue 33447:https://bugs.python.org/issue33447
.. _coroutine: https://docs.python.org/3/glossary.html#term-coroutine

For example, it is fairly common to specify code contracts as lambdas using
a library such as `icontract`_ than writing every trivial contract in a separate
function.

.. _icontract: https://github.com/Parquery/icontract

**Micro**.
*Awaited* is thought of and implemented as a *micro*-library.
This means that we strongly limit it scope and aim for the simplest implementation
possible so that you can embed it directly into your code base, if you prefer to avoid
adding yet another dependency to your project.

In fact, it is so *micro* that it fits less than `25 lines of code`_.
We provide a `PyPI package`_ simply for your convenience if you opt in for it as
a dependency nevertheless.

.. _25 lines of code: https://github.com/mristin/awaited/awaited/__init__.py
.. _PyPI package: https://pypi.org/project/awaited/

**Better with `asyncstdlib`_**.
*Awaited* plays really well with `asyncstdlib`_, which you can use for further
chaining on async generators.
It gives you a primitive transformation from a sync iterable of awaitables to
an async iterable of awaited values.
The `asyncstdlib`_ can pick it up from there.

**Standardized interface**.
In the future, tools such as `icontract-hypothesis`_ might include it in their analysis.
Having a standardized set of canonical operations (as *awaited* provides) makes the
job of the analysis tools a bit easier.
For example, they can directly check for equivalence to identify the operations
comparing the addresses of the functions.

.. _icontract-hypothesis: https://github.com/mristin/icontract-hypothesis

Usage
=====
We present here the interface of the library and show how it is meant to be used.

``awaited.then`` awaits a coroutine and applies a function on the awaited result:

.. code-block:: python

    >>> import awaited

    >>> async def some_func() -> List[int]:
    ...     return [1, 2, 3]

    # some_func() gives a coroutine!
    >>> awaited_sum = await awaited.then(some_func(), sum)
    6

``awaited.these`` awaits each item of a sync iterable of *awaitables* resulting
in an async iterable of awaited items:

.. code-block:: python

    >>> import asyncstdlib

    >>> async def async_is_non_negative(x: int) -> bool:
    ...     return x > 0

    >>> all_non_negative = await asyncstdlib.all(
    ...     awaited.these(
    ...         async_is_non_negative(x) for x in [1, 2, 3]))
    True

Installation
============
You can install the library using `pip` in your virtual environment:

.. code-block::

    pip3 install awaited

Related Projects
================

* **`asyncstdlib`_** helps you work with async callables, iterables and
  context managers.

  Asyncstdlib is a much bigger library than *awaited* and can not be readily used for
  a replacement of async lambdas (see `the asyncstdlib issue 27`_).

.. _asyncstdlib: https://github.com/maxfischer2781/asyncstdlib
.. _the asyncstdlib issue 27: https://github.com/maxfischer2781/asyncstdlib/issues/27

Versioning
==========

We follow `Semantic Versioning <http://semver.org/spec/v1.0.0.html>`_.
The version X.Y.Z indicates:

* X is the major version (backward-incompatible),
* Y is the minor version (backward-compatible), and
* Z is the patch version (backward-compatible bug fix).