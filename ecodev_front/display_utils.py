"""
Component helpers to ease display of data to be presented.
"""
from math import floor
from math import log

from ecodev_front.constants import BILLION
from ecodev_front.constants import MILLION
from ecodev_front.constants import THOUSAND
from ecodev_front.constants import TRILLION


def number_formatting(number: float, decimals: int = 0) -> str:
    """
    Returns numbers in a more readable format (scaled with suffix).
    """
    units = ['', 'K', 'M', 'G', 'T', 'P']
    k = 1000.0
    magnitude = int(floor(log(number, k)))
    return f'%.{decimals}f %s' % (number / k ** magnitude, units[magnitude])


def get_magnitude(number: int | float) -> tuple[object, str]:
    """
    Returns the metric to divide by and the unit
    """
    units = ['', 'K', 'M', 'B', 'T', 'P']
    denominator = [1, THOUSAND, MILLION, BILLION, TRILLION, 'P']

    k = 1000.0
    magnitude = int(floor(log(number, k)))

    return denominator[magnitude], units[magnitude]
