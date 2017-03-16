#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = global-statement
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = redefined-outer-name

# ------------------
# GlobalVariables.py
# ------------------

# https://docs.python.org/3/reference/simple_stmts.html#grammar-token-nonlocal_stmt

print("GlobalVariables.py")

x1 = 0

def f1 () :
    x1 = 1

    def g1 () :
        x1 = 2
        assert x1 == 2

    g1()
    assert x1 == 1

f1()
assert x1 == 0



x2 = 0

def f2 () :
    x2 = 1

    def g2 () :
        nonlocal x2
        x2 = 2

    g2()
    assert x2 == 2

f2()
assert x2 == 0



x3 = 0

def f3 () :
    global x3
    x3 = 1

    def g3 () :
        global x3
        x3 = 2

    g3()
    assert x3 == 2

f3()
assert x3 == 2

print("Done.")
