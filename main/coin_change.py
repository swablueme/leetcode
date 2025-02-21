from threading import local
from typing import List
import math
from functools import lru_cache


def change(coins: List[int], amount: int):
    coin_amounts = {}
    coins = tuple(coins)

    def coinChange(amount: int) -> int:
        if amount == 0:
            return 0
        elif amount < 0:
            return math.inf
        elif amount > 0:
            if amount in coin_amounts:
                return coin_amounts[amount]
            else:
                min_value = min([1 + coinChange(amount - coin)
                                 for coin in coins])
                coin_amounts[amount] = min_value
                return min_value
    found = coinChange(amount)
    return -1 if found == math.inf else found


assert change([1, 2, 5], 11) == 3
assert change([1, 5, 10], 12) == 3
assert change([2], 3) == -1
assert change([3, 1, 4], 1) == 1
assert change([1], 0) == 0
