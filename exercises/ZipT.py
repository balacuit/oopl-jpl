#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------
# ZipT.py
# -------

# https://docs.python.org/3/library/functions.html#zip

from unittest import main, TestCase

from Zip import  \
    my_zip_iter, \
    my_zip_map

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            my_zip_iter,
            my_zip_map,
            zip]

    def test_1 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(list(f()), [])

    def test_2 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(list(f([])), [])

    def test_3 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(list(f((), ())), [])

    def test_4 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(list(f([2, 3])), [(2,), (3,)])

    def test_5 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(list(f((2, 3), (4, 5), (6, 7))), [(2, 4, 6), (3, 5, 7)])

    def test_6 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(list(f([2, 3, 4], [5, 6, 7])), [(2, 5), (3, 6), (4, 7)])

if __name__ == "__main__" :
    main()
