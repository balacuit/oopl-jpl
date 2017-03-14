#!/usr/bin/env python3
""" Reduce.py
"""
def reduce_for_range(method, list_of_something, seed):
    """ Reduce by iterating over a range.
    """
    for i in range(len(list_of_something)):
        seed = method(seed, list_of_something[i])
    return seed


def reduce_for_enumerate(method, list_of_something, seed):
    """ Reduce by iterating over an enumeration.
    """
    for i, item in enumerate(list_of_something):
        seed = method(seed, item)
    return seed

def reduce_for(method, list_of_something, seed):
    """ Reduce by looping with a for.
    """
    for i in list_of_something :
        seed = method(seed, i)
    return seed

def reduce_while(method, list_of_something, seed):
    """ Reduce by looping with a while.
    """
    i = iter(list_of_something)
    try:
        while True:
            seed = method(seed, next(i))
    except StopIteration :
        pass
    return seed

if __name__ == "__main__" :
    from operator  import add, sub
    reduce_while(sub, [2,3,4], 1)