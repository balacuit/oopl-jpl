# -----------
# Mon, 13 Mar
# -----------

"""
Collatz Conjecture

take a pos int
if even, divide by 2
if odd, multiply by 3 and add 1
repeat, until 1

5 16 8 4 2 1

cycle length of  5 is 6
cycle length of 10 is 7
"""

class A (B) :
    t = 5

    def __init__ (self, n) :
        self.x = n

    def f (self, y) :
        return self.x * y

    @staticmethod
    def g (z) :
        return A.t + z**2

# Java
# A m = new A(2)

m = A(2)
print(m.f(3)) # 6

print(A.g(4)) # 16

"""
first exercise, IsPrime1

1. run it as is, confirm success

2. identify the broken tests
   fix test
   run it, confirm failures

3. identify the broken code
   fix code
   run it, confirm success
"""

"""
pretend that Python doesn't have exceptions

1. use the return facility
2. use a parameter that you know is by address
3. use a global
"""

def f (...) :
    ...
    if (<something wrong>)
        raise Tiger(...)
    ...

def g (...) :
    ...
    try :
        ...
        x = f(...)
        ...
    except Tiger as e :
        ...
        raise e
    except Mammal as e :
        <something wrong>
    else :
        ...
    finally :
        ...
    ...

...
g(...)
...

"""
Java:

A x = new A(...);
A y = new A(...);

S.O.P(x == y);     // false
S.O.P(x.equals(y); // true
"""

x = [2, 3.4, [5]]
print(type(x))      # list
x[0] = 5
print(x)            # [5, 3.4, [5]]
x += [6, 7]
print(x)            # [5, 3.4, [5], 6, 7]

x = (2, 3.4, [5])
print(x)            # (2, 3.4, [5])
print(type(x))      # tuple
x[0]    = 5         # not ok
x[2][0] = 6
print(x)            # (2, 3.4, [6])

x = [2]
print(type(x)) # list
print(len(x))  # 1

x = (2)
print(type(x)) # int
print(len(x))  # not ok

x = (2,)
print(type(x)) # tuple
print(len(x))  # 1

print(type(list))  # type
print(type(int))   # type
print(type(tuple)) # type

print(type(type))  # type

x = list()
print(type(x)) # list
print(len(x))  # 0
print(x)       # []

x = tuple()
print(type(x)) # tuple
print(len(x))  # 0
print(x)       # ()

x = int()
print(type(x)) # int
print(len(x))  # not ok
print(x)       # 0

def f (g, x, y, z) :
    return g(x, y) + g(y, z)

def plus (x, y) :
    return x + y

print(f(plus, 2, 3, 4)) # 12
print(f(+,    2, 3, 4)) # not ok
print(f(add,  2, 3, 4)) # 12

print(f(lambda x, y : x + y, 2, 3, 4)) # 12

i = 2
j = 3
k = (i + j)
i + j       # not ok
i = j
k = (i = j) # not ok
(i + j) = k # not ok

# expressions can not standalone
# must be used in something larger

# statements can standalone
# can not be in something larger

i += j
k = (i += j) # not ok
(i += j) = k # ok in C++

# unary
~, -, not, *, **

# binary
=, +, +=, -, -+, *, *=, /, /=, %, %=, and, or

# ternary
if else

# n-ary
()
