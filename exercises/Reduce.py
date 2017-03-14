#!/usr/bin/env python3
""" Implement Reduce in 4 ways.
"""
def reduce_for_range(method: Callable([T,T], T),
                     a: Sequence,
                     seed: T) -> int:
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
    for i in a :
        seed = method(seed, i)
    return seed

def reduce_while(method, a, seed) -> int:
    """ Reduce by looping with a while.
    """
    i = iter(a)
    try:
        while True:
            seed = method(seed, next(i))
    except StopIteration :
        pass
    return seed

if __name__ == "__main__" :
    from operator  import add, sub
    print(reduce_while(sub, [2,3,4], 1))