import functools


def climbStairs(n: int) -> int:

    @functools.lru_cache(maxsize=100, typed=False)
    def climb(n):
        if n == 0:
            return 1
        elif n < 0:
            return 0
        else:
            return climb(n - 1) + climb(n - 2)
    return climb(n)


if __name__ == "__main__":
    print(climbStairs(30))
