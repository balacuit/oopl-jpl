#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -----------
# Reduce2T.py
# -----------

# https://docs.python.org/3/library/functools.html

from functools import reduce
from operator  import add, sub
from unittest  import main, TestCase

from Reduce2 import \
    reduce_1,       \
    reduce_2

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            reduce_1,
            reduce_2,
            reduce]

    def test_1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertRaises(TypeError, f, None, [])

    def test_2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(None, [],       2),  2)

    def test_3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(None, [2]),          2)

    def test_4 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(add, [2],       1),  3)

    def test_5 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(add, [2, 3, 4]),     9)

    def test_6 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(add, [2, 3, 4], 1), 10)

    def test_7 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(sub, [2, 3, 4]),    -5)

    def test_8 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(sub, [2, 3, 4], 1), -8)

if __name__ == "__main__" :
    main()
