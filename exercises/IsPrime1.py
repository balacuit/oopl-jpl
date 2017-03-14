#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -----------
# IsPrime1.py
# -----------

from math import sqrt

def is_prime (n: int) -> int  :
    assert n > 0
    if (n == 2) :  # 2 is prime
        return True
    if (n == 1) or ((n % 2) == 0) :
        return False
    for i in range(3, int(sqrt(n))+1, 2) :  # extend range, skip even numbers
        if (n % i) == 0 :
            return False
    return True
