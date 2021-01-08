"""
Climbing Stairs
You are climbing a staircase.
It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
---
Basically, it's fibonacci
"""


def climb_stairs(n):
    if n <= 0: return 0
    if n <= 2: return n

    all_steps = 0
    two_steps_before = 1
    one_step_before = 2

    for i in range(3, n + 1, 1):
        all_steps = one_step_before + two_steps_before
        two_steps_before = one_step_before
        one_step_before = all_steps

    return all_steps
