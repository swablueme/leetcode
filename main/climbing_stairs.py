import functools


def climbStairs(n: int) -> int:
    global values
    values = 0

    @functools.lru_cache(maxsize=100, typed=False)
    def climb(n, lst):
        global values
        if n == 0:
            values += 1
        elif n < 0:
            values += 0
        else:
            for value in [1, 2]:
                climb(n - value, lst + (value,))
    climb(n, ())
    return values


print(climbStairs(30))
