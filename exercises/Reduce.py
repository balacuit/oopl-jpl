#!/usr/bin/env python3
""" Implement Reduce in 4 ways.
"""


def reduce_for_range(method, a, seed) -> int:
    """ Reduce by iterating over a range.
    """
    for i in range(len(a)):
        seed = method(seed, a[i])
    return seed


def reduce_for_enumerate(method, a, seed) -> int:
    """ Reduce by iterating over an enumeration.
    """
    for _, item in enumerate(a):
        seed = method(seed, item)
    return seed


def reduce_for(method, a, seed) -> int:
    """ Reduce by looping with a for.
    """
    for i in a:
        seed = method(seed, i)
    return seed


def reduce_while(method, a, seed) -> int:
    """ Reduce by looping with a while.
    """
    i = iter(a)
    try:
        while True:
            seed = method(seed, next(i))
    except StopIteration:
        pass
    return seed


if __name__ == "__main__":
    from operator import add, sub
    print(reduce_while(sub, [2, 3, 4], 1))


# pylint: disable = bad-whitespace
# pylint: disable = consider-using-enumerate
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------
# Reduce.py
# ---------

from typing import Callable, Iterable, Sequence, TypeVar

T = TypeVar('T')


def reduce_for_range(bf: Callable[[T, T], T], a: Sequence[T], v: T):
    for i in range(len(a)):
        w = a[i]
        v = bf(v, w)
    return v


def reduce_for_enumerate(bf: Callable[[T, T], T], a: Sequence[T], v: T):
    for i, _ in enumerate(a):
        w = a[i]
        v = bf(v, w)
    return v


def reduce_for(bf: Callable[[T, T], T], a: Iterable[T], v: T):
    for w in a:
        v = bf(v, w)
    return v


def reduce_while(bf: Callable[[T, T], T], a: Iterable[T], v: T):
    p = iter(a)
    try:
        while True:
            w = next(p)
            v = bf(v, w)
    except StopIteration:
        pass
    return v
