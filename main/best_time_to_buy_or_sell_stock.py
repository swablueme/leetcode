from typing import List
import math


def maxProfit(prices: List[int]) -> int:
    max_index, max_price = None, 0
    min_index, min_price = None, 0
    best_cost = 0

    if len(prices) < 2:
        return 0
    for idx in range(len(prices)):
        price = prices[idx]
        isBetterMin = True if price < min_price else False
        isBetterMax = True if price >= max_price else False

        # min not initialised
        if min_index == None:
            min_index = idx
            min_price = price
        elif isBetterMin and (max_index == None or idx < max_index):
            min_index = idx
            min_price = price
        elif isBetterMax and idx > min_index:
            max_index = idx
            max_price = price
        elif isBetterMin and idx > max_index:
            # reset
            best_cost = max(best_cost, max_price - min_price)
            min_index = idx
            min_price = price
            max_index = None
            max_price = 0
    if max_index != None:  # another was found after the reset
        best_cost = max(best_cost, max_price - min_price)
    return best_cost


assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert maxProfit([7, 6, 4, 3, 1]) == 0
assert maxProfit([7]) == 0
assert maxProfit([2, 4, 1, 4, 0, 4]) == 4
assert maxProfit([2, 4, 1]) == 2
