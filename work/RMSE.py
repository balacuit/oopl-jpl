""" root-mean-square error
"""
# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement
# pylint: disable = unused-argument
# pylint: disable = unused-import

from functools import reduce
from operator import sub

import numpy as np


def rmse_for_range(predictions, targets):
    """ Calculate RMSE using for and range.

    :param targets: list
    :param predictions: list
    """
    diffs = []
    for i in range(0, len(predictions)):
        diff = predictions[i] - targets[i]
        diffs.append(diff**2)

    sums = 0
    for i in diffs:
        sums += i

    mean = sums/len(diffs)

    return int(mean**0.5)


def rmse_for_enumerate(predictions, targets):
    """ Calculate RMSE using a for and enumerate()

    TODO
    :param targets: list
    :param predictions: list
    """
    diffs = []
    for i in range(0, len(predictions)):
        diff = predictions[i] - targets[i]
        diffs.append(diff**2)

    sums = 0
    for i in diffs:
        sums += i

    mean = sums/len(diffs)

    return int(mean**0.5)


def rmse_iterator(predictions, targets):
    """ Calculate RMSE using an iterator

    TODO
    :param targets: list
    :param predictions: list
    """
    diffs = []
    for i in range(0, len(predictions)):
        diff = predictions[i] - targets[i]
        diffs.append(diff**2)

    sums = 0
    for i in diffs:
        sums += i

    mean = sums/len(diffs)

    return int(mean**0.5)


def rmse_map_sum(predictions, targets):
    """ Calculate RMSE using map() and sum()

    TODO
    :param targets: list
    :param predictions: list

    """
    diffs = []
    for i in range(0, len(predictions)):
        diff = predictions[i] - targets[i]
        diffs.append(diff**2)

    sums = sum(diffs)

    mean = sums/len(diffs)

    return int(mean**0.5)


def rmse_zip_for(predictions, targets):
    """ Calculate RMSE using zip() and for

    :param targets: list
    :param predictions: list
    """
    diffs = []
    for i, j in zip(predictions, targets):
        diffs.append((i - j)**2)

    sums = 0
    for i in diffs:
        sums = sums + i
    mean = sums/len(diffs)

    return int(mean**0.5)


def rmse_zip_map_sum(predictions, targets):
    """ Calculate RMSE using zip(), map() and sum()
    """
    zips = list(zip(predictions, targets))

    diffs = list(map(lambda x: (x[0]-x[1])**2, zips))

    sums = sum(diffs)

    mean = sums/len(predictions)

    return int(mean**0.5)


def rmse_zip_list_sum(predictions, targets):
    """ Calculate RMSE using zip(), list(), and sum()
    """
    zips = list(zip(predictions, targets))

    # TODO use list ?
    diffs = list(map(lambda x: (x[0]-x[1])**2, zips))

    sums = sum(diffs)

    mean = sums/len(diffs)

    return int(mean**0.5)


def rmse_zip_generator_sum(predictions, targets):
    """ Calculate RMSE using zip(), a generator, and zip()
    """
    zips = list(zip(predictions, targets))

    diffs = list(((a - b)**2 for a,b in zips))

    sums = sum(diffs)

    mean = sums/len(diffs)

    return int(mean**0.5)


def rmse_numpy(predictions, targets):
    """ Ref: http://stackoverflow.com/questions/21926020/
    """
    return np.sqrt(((np.array(predictions) - np.array(targets)) ** 2).mean())
