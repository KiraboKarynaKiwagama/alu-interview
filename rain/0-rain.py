#!/usr/bin/python3
"""Rainwater retention calculation"""


def rain(walls):
    """Return the total units of rainwater retained between walls.

    Uses two pointers moving inward from both ends. Water above a
    position is limited by the shorter of the tallest walls on its
    left and right sides.
    """
    if not walls:
        return 0

    left, right = 0, len(walls) - 1
    left_max, right_max = walls[left], walls[right]
    total = 0

    while left < right:
        if walls[left] < walls[right]:
            left += 1
            left_max = max(left_max, walls[left])
            total += left_max - walls[left]
        else:
            right -= 1
            right_max = max(right_max, walls[right])
            total += right_max - walls[right]

    return total