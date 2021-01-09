"""
Fibonacci Number
0 1 1 2 3 5 8 13 21 34 55
Constraint : 0 <= n <= 30
"""


def fib(n):
    cache = {0: 0, 1: 1}

    if n not in cache: cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]
