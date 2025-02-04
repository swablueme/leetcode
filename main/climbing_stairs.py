import functools


def climbStairs(n: int) -> int:
    values = set()

    @functools.lru_cache(maxsize=100, typed=False)
    def climb(n, lst):
        if n == 0:
            values.add(lst)
        elif n < 0:
            return
        else:
            for value in [1, 2]:
                climb(n - value, lst + (value,))

    climb(n, ())
    return values


print(climbStairs(30))
