#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# --------
# RMSET.py
# --------

from timeit   import timeit
from unittest import main, TestCase

from RMSE import            \
    rmse_for_range,         \
    rmse_for_enumerate,     \
    rmse_iterator,          \
    rmse_map_sum,           \
    rmse_zip_for,           \
    rmse_zip_map_sum,       \
    rmse_zip_list_sum,      \
    rmse_zip_generator_sum, \
    rmse_numpy

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            rmse_for_range,
            rmse_for_enumerate,
            rmse_iterator,
            rmse_map_sum,
            rmse_zip_for,
            rmse_zip_map_sum,
            rmse_zip_list_sum,
            rmse_zip_generator_sum,
            rmse_numpy,
            ]
    def test_1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f((2, 3, 4), (2, 3, 4)), 0)

    def test_2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f((2, 3, 4), (3, 2, 5)), 1)

    def test_3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f((2, 3, 4), (4, 1, 6)), 2)

    def test_4 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f((1, 2, 3, 4, 5), (2, 5, 3, 1, 4)), 2)

    def test_5 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                print()
                print(f.__name__)
                t = timeit(
                    f.__name__ + "(10000 * [1], 10000 * [5])",
                    "from __main__ import " + f.__name__,
                    number = 100)
                print("{:.2f} milliseconds".format(t * 1000))

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% python3.5 RMSET.py
....
rmse_range_for
418.78 milliseconds

rmse_iterator
520.41 milliseconds

rmse_map_sum
428.75 milliseconds

rmse_zip_for
401.01 milliseconds

rmse_zip_map_sum
524.03 milliseconds

rmse_zip_list_sum
377.73 milliseconds

rmse_zip_generator_sum
383.78 milliseconds

rmse_numpy
134.99 milliseconds
.
----------------------------------------------------------------------
Ran 5 tests in 3.195s

OK
"""
