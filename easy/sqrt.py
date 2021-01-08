"""
Sqrt(x)

Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated,
and only the integer part of the result is returned.

---
Newton's method
"""


def sqrt(x):
    result = x

    while result * result > x:
        result = (result + x / result) / 2

    return int(result)


if __name__ == '__main__':
    assert sqrt(4) == 2
    assert sqrt(8) == 2
    assert sqrt(0) == 0
    assert sqrt(1) == 1
    assert sqrt(2) == 1
    assert sqrt(100) == 10
