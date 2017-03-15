class Map_Iterator:

    def __init__(self, f, a):
        """  """
        self.f = f
        self.i = iter(a)

    def __iter__(self):
        """ """
        return self

    def __next__(self):
        return self.f(next(self.i))


def map_for_range(f, x):
    for i in range(len(x)):
        yield f(x[i])


def map_for_enumerate(f, x):
    for i, _ in enumerate(x):
        yield f(x[i])


def map_for(f, x):
    for i in x:
        yield f(i)


def map_generator(f, x):
    return (f(i) for i in x)
