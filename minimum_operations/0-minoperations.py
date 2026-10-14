#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Return the fewest operations (Copy All / Paste) needed to get
    exactly n 'H' characters, starting from a single 'H'.

    Returns 0 if n is impossible to achieve.
    """
    if not isinstance(n, int) or n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
