"""
Component helpers to ease display of data to be presented.
"""
from math import floor
from math import log


def number_formatting(number: float) -> str:
    """
    Returns numbers in a more readable format (scaled with suffix).
    """
    units = ['', 'K', 'M', 'G', 'T', 'P']
    k = 1000.0
    magnitude = int(floor(log(number, k)))
    return '%.2f %s' % (number / k ** magnitude, units[magnitude])
