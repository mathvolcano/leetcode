"""
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3299/
"""


def stringShift(s, shift) -> str:
    if (len(shift) == 0) or (len(s) == 0): return s

    net_shift_right = 0
    for sh in shift:
        net_shift_right += -sh[1] if sh[0] == 0 else sh[1]

    net_left = (-net_shift_right) % len(s)
    return s[net_left:] + s[:net_left]