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
        raise E(...)
    ...

def g (...) :
    ...
    try :
        ...
        x = f(...)
        ...
    except G as e :
        <something wrong>
    ...

...
g(...)
...











































