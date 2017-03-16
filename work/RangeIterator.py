
class Range_Iterator:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.end:
            i = self.i
            self.i += 1
            return i

        raise StopIteration


def range_iterator_yield(start, end):
    while start < end:
        yield start
        start+=1
