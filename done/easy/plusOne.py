"""
Plus One

Given a non-empty array of decimal digits representing a non-negative integer.
Increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
"""


def plus_one(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] != 9:
            digits[i] += 1
            break
        else:
            digits[i] = 0

    # initial array consists only 99..
    if digits[0] == 0:
        digits.insert(0, 1)

    return digits
