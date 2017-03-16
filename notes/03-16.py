# -----------
# Thu, 16 Mar
# -----------

def f () :
    yield 2
    yield 3
    yield 4

x = f()
print(x is iter(x)) # true

print(list(x)) # [2, 3, 4]
print(list(x)) # []

print(list(f())) # [2, 3, 4]
print(list(f())) # [2, 3, 4]

r = range(2, 5)
print(type(r))   # <range>

p = iter(r)
print(type(p))   # <range_iterator>

"""
% FileInputOutput.py

"""

x = [2, 3, 4]
y = x

print(x is y) # true
print(x == y) # true

x = [2, 3, 4]
y = [2, 3, 4]

print(x is y) # false
print(x == y) # true

class A :
    def __init__ (self, i = 81, j = 6) :
        ...

    def __eq__ (self, rhs) :
        ...

x = A()
y = A(2)
z = A(2, 3)

x = A(2, 3)
y = x

print(x is y) # true

x = A(2, 3)
y = A(2, 3)

print(x is y) # false
print(x == y) # print(x.__eq__(y)) # true

"""
if you do NOT define ==, == becomes is
"""

"""
<expr> if <cond> else <expr>
"""

x = A(2)
y = A(2)
print(x is y) # false

x = A
y = A
print(x is y) # true

# three tokens: =, *, **
# two contexts: function call, function definition

print("abc", end=" ")




























