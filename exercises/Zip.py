#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ------
# Zip.py
# ------

def my_zip_iter (*a) :
    if not a :
        return iter(a)
    x = [iter(v) for v in a]
    for _ in a[0] :
        y = [next(v) for v in x]
        yield tuple(y)

def my_zip_map (*a) :
    if not a :
        return iter(a)
    return map(lambda *a : a, *a)
