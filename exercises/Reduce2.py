#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ----------
# Reduce2.py
# ----------

def reduce_1 (bf, a, *v) :
    if not a and not v :
        raise TypeError("reduce() of empty sequence with no initial value")
    p = iter(a)
    if not v :
        v = next(p)
    else :
        v = v[0]
    for w in p :
        v = bf(v, w)
    return v

def reduce_2 (bf, a, *v) :
    p = iter(a)
    if not v :
        if not a :
            raise TypeError("reduce() of empty sequence with no initial value")
        v = next(p)
    else :
        v = v[0]
    for w in p :
        v = bf(v, w)
    return v
