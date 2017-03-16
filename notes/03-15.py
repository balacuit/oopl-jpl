# -----------
# Wed, 15 Mar
# -----------

a = [2, 3, 4]
print(a[0])   # 2
print(a[1])   # 3
print(a[2])   # 4
print(a[3])   # IndexError

"""
1 2 -> -1 -> 1
2 5 -> -3 -> 9
3 3 ->  0 -> 0
4 1 ->  3 -> 9
5 4 ->  1 -> 1

mean -> 4
sqrt -> 2
"""

a = [2, 3, 4]

print(list(range(len(a)))) # [0, 1, 2]

print(list(enumerate(a)))  # [(0, 2), (1, 3), (2, 4)]

for v in a :
    ...

# a must be iterable over anything

for u, v in a :
    ...

# a must be iterable over iterable of length 2

for u, v in [(2, 3), [3, 4], {4, 5}] :
    ...

a = [2, 3, 4]
b = [5, 6, 7]

print(list(zip(a, b))) # [(2, 5), (3, 6), (4, 7)]

def f () :
    print("abc")
    yield 2
    print("def")
    yield 3
    print("ghi")
    yield 4

p = f()     # nothing prints

q = iter(p)
print(p is q) # true

v = next(p) # abc
print(v)    # 2

v = next(p) # def
print(v)    # 3

v = next(p) # ghi
print(v)    # 4

v = next(p) # StopIteration

# define map in two ways
# 1. as a class that reponds to __next__, __init___, __iter__
# 2. as a function with yield

m = map(...)
print(list(m))

x = range(2, 5)
print(x)        # <range object at <addr>>
v = next(x)     # not ok
print(list(x))  # [2, 3, 4]
print(list(x))  # [2, 3, 4]

p = iter(x);
print(x is p)   # false

print(list(p))  # [2, 3, 4]
print(list(p))  # []

q = iter(p)
print(p is q)   # true

m = map(lambda..., [2, 3, 4])

r = range_iterator(2, 5)

class map_iterator :
    def __init__ (self, uf, a) :

class A :
    class B :
        def __init (self, j) :
            self.j = j

    def __init__ (self, i) :
        self.i = i

    def __iter__ (self) :
        return A.B(3)

x = A(2)
print(type(x)) # A

y = x.g()
print(type(y)) # A.B
