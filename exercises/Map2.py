#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------
# Map2.py
# -------

def map_iter_yield (nf, *a) :
    x = [iter(v) for v in a]
    for _ in a[0] :
        y = [next(v) for v in x]
        yield nf(*y)

def map_zip_yield (nf, *a) :
    for v in zip(*a) :
        yield nf(*v)

def map_zip_generator (nf, *a) :
    return (nf(*v) for v in zip(*a))
