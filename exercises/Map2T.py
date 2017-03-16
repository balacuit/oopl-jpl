#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# --------
# Map2T.py
# --------

# https://docs.python.org/3/library/functions.html#map

from unittest import main, TestCase

from Map2 import      \
    map_iter_yield,   \
    map_zip_yield,    \
    map_zip_generator

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            map_iter_yield,
            map_zip_yield,
            map_zip_generator]

    def test_1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(lambda v : v ** 3, [2, 3])
                self.assertEqual(list(x), [8, 27])
                self.assertEqual(list(x), [])

    def test_2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(lambda v, w : v ** w, (2, 3), (2, 3))
                self.assertEqual(list(x), [4, 27])
                self.assertEqual(list(x), [])

if __name__ == "__main__" :
    main()
