

def climbStairs(n: int) -> int:
    values = []

    def climb(n, lst, values):
        if n == 0:
            values.append(lst)
        elif n < 0:
            return
        else:
            for value in [1, 2]:
                climb(n - value, lst + (value,), values)

    climb(n, (), values)
    return values
