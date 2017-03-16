#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ----------
# Reduce2.py
# ----------

def reduce_while (bf, a, *v) :
    if not a and not v :
        raise TypeError("reduce() of empty sequence with no initial value")
    p = iter(a)
    if v :
        v = v[0]
    else :
        v = next(p)
    try :
        while True :
            v = bf(v, next(p))
    except StopIteration :
        pass
    return v

def reduce_for (bf, a, *v) :
    if not a and not v :
        raise TypeError("reduce() of empty sequence with no initial value")
    p = iter(a)
    if v :
        v = v[0]
    else :
        v = next(p)
    for w in p :
        v = bf(v, w)
    return v
