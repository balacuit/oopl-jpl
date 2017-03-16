class Range_1:
    """
    """
    class Iterator () :
        def __init__ (self, b: int, e: int) -> None :
            self.b = b
            self.e = e

        def __iter__ (self) -> "Range_Iterator" :
            return self

        def __next__ (self) -> int :
            if self.b == self.e :
                raise StopIteration()
            v = self.b
            self.b += 1
            return v

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        """ Return a new instance of the range iterator
        """
        return Range_1.Iterator(self.start, self.end)


class Range_2:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        start = self.start
        while start != self.end :
            yield start
            start += 1