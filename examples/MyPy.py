#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = line-too-long
# pylint: disable = missing-docstring

# -------
# MyPy.py
# -------

from typing import Dict, Iterable, Iterator, List, Sequence, Set, Tuple

print("MyPy.py")

def f () -> None :
    pass

f()
# x = f() # MyPy.py:25: error: "f" does not return a value



def f_int (n: int) :
    assert n

f_int(2)
# f_int(2.3) # MyPy.py:21: error: Argument 1 to "g" has incompatible type "float"; expected "int"



def f_list (a: List[int]) :
    assert a

f_list([2, 3, 4])
# f_list([2, 3.4, 5]) # MyPy.py:31: error: List item 1 has incompatible type "float"
# f_list((2, 3, 4))   # MyPy.py:37: error: Argument 1 to "f_list" has incompatible type "Tuple[int, int, int]"; expected List[int]



def f_tuple (a: Tuple[int, str]) :
    assert a

f_tuple((2, "abc"))
# f_tuple(("abc", 2)) # MyPy.py:37: error: Argument 1 to "f_tuple" has incompatible type "Tuple[str, int]"; expected "Tuple[int, str]"
# f_tuple([2, "abc"]) # MyPy.py:46: error: Argument 1 to "f_tuple" has incompatible type List[object]; expected "Tuple[int, str]"



def f_sequence (a: Sequence[int]) :
    assert a

f_sequence([2, 3, 4])
f_sequence((2, 3, 4))
# f_sequence((2, 3.4, 5)) # MyPy.py:55: error: Argument 1 to "f_sequence" has incompatible type "Tuple[int, float, int]"; expected Sequence[int]
# f_sequence({2, 3, 4})   # MyPy.py:56: error: Argument 1 to "f_sequence" has incompatible type Set[int]; expected Sequence[int]



def f_set (a: Set[int]) :
    assert a

f_set({2, 3, 4})
# f_set({2, 3.4, 5}) # MyPy.py:54: error: Argument 2 to <set> has incompatible type "float"; expected "int"
# f_set([2, 3, 4])   # MyPy.py:54: error: Argument 1 to "f_set" has incompatible type List[int]; expected Set[int]



def f_dict (a: Dict[int, str]) :
    assert a

f_dict({2: "abc", 3: "def", 4: "ghi"})
# f_dict({2: "abc", "def": 3, 4: "ghi"}) # MyPy.py:73: error: List item 1 has incompatible type "Tuple[str, int]"



def f_iterable (a: Iterable[int]) :
    assert a

f_iterable([2, 3, 4])
f_iterable((2, 3, 4))
f_iterable({2, 3, 4})
f_iterable({2: "abc", 3: "def", 4: "ghi"})
f_iterable((map(lambda v : v**2, (2, 3, 4))))
# f_iterable(2)                               # MyPy.py:63: error: Argument 1 to "f_iterable" has incompatible type "int"; expected Iterable[int]



def f_iterator (a: Iterator[int]) :
    assert a

f_iterator((map(lambda v : v**2, (2, 3, 4))))
# f_iterator([2, 3, 4])                       # MyPy.py:63: error: Argument 1 to "f_iterator" has incompatible type List[int]; expected Iterator[int]

print("Done.")
