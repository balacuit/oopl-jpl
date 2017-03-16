
def reduce_for(f, l, *s):

    if not l and not s:
        raise TypeError
    i = iter(l)

    if s:
        v = s[0]
    else:
        v = next(i)

    for j in i:
        v = f(v, j)

    return v


def reduce_while(f, l, *s):

    if not l and not s:
        raise TypeError
    i = iter(l)

    if s:
        v = s[0]
    else:
        v = next(i)
    try:
        while True:
            v = f(v, next(i))
    except StopIteration as e:
        pass
    return v
