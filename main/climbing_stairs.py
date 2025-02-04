import functools


def climbStairs(n: int) -> int:

    @functools.lru_cache(maxsize=100, typed=False)
    def climb(n, lst):
        if n == 0:
            return 1
        elif n < 0:
            return 0
        else:
            return climb(n - 1, lst + (1,)) + climb(n - 2, lst + (2,))
    return climb(n, ())


print(climbStairs(30))
