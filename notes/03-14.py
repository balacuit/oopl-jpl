# -----------
# Tue, 14 Mar
# -----------

a = [2, 3, 4]
b = [2, 3, 4]
print(a is b) # false
print(a == b) # true

a = [2, 3, 4]
b = a
print(a is b) # true
print(a == b) # false

a = [2, 3, 4]
print(type(a)) # list
p = iter(a)
print(type(p)) # list iterator
v = next(p)
print(v)       # 2
v = next(p)
print(v)       # 3
v = next(p)
print(v)       # 4
v = next(p)    # raises StopIteration

for v in a :
    ...

"""
a must be iterable
iterable means:

1. respond iter()
2. the response responds to next()
3. next() is used repeatedly until exhaustation and it raises StopIteration
"""

"""
List's += operator takes an iterable on the right hand side
"""

a = (2, 3)
print(type(a)) # tuple
print(len(a))  # 2

a = (2)
print(type(a)) # int

a = (2,)
print(type(a)) # tuple

i = 2
j = 3
i += j
print(i) # 5
print(j) # 3

i = 2
j = 3
i = i + j
print(i) # 5
print(j) # 3

"""
x += y        is the same as       x = x + y

true  for tuples
false for lists
"""

"""
List's + operator takes a list on the right hand side
"""

"""
Tuple's += operator takes a tuple on the right hand side
"""

"""
Tuple's + operator takes a tuple on the right hand side
"""

def reduce (bf, a: Sequence, v) :
    for i in range(len(a)) :
        w = a[i]
        v = bf(v, w)
    return v

def reduce (bf, a: Iterable, v) :
    for w in a :
        v = bf(v, w)
    return v

for v in a :
    ...

for u, v in a :
    ...

class A :
    def __iter__ (self) :
        ...

x = A()
...__init__()...

iter(x)
x.__iter__()

len(x)
x.__len__()

next(x)
x.__next__()

x[2]
x.__getitem__(2)

x(2, 3, 4)
x.__call__(2, 3, 4)

a = [2, 3, 4]
print(a[i]) # 3
a[i] = 5
print(a)    # [2, 5, 4]

a = [2, 3, 4]
print(type(a)) # list

p = iter(a)
print(type(p)) # list iterator
print(a is p)  # false

q = iter(a)
print(type(q)) # list iterator
print(a is q)  # false

print(p is q)  # false

r = iter(p)
print(p is r)  # true

a = [2, 3, 4, ...]
for v in a :
    f(v)

a = [2, 3, 4, ...]
p = iter(a)
f(next(p))   # the first  item
f(next(p))   # the second item
f(next(p))   # the third  item
for v in p : # the rest of the items
    g(v)
