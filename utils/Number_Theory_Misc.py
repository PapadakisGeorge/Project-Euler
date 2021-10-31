from functools import reduce

from sympy import gcd


def lowest_common_denominator(number_1, number_2):
    return number_1 * number_2 // gcd(number_1, number_2)


def lowest_common_denominator_multiple(*numbers):
    return reduce(lowest_common_denominator, numbers)