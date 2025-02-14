from typing import List
import math
# def maxProfit(prices: List[int]) -> int:
#     max_index = None
#     min_index = None
#     best_cost = 0

#     if len(prices) < 2:
#         return 0
#     for idx in range(len(prices)):
#         price = prices[idx]
#         min_price = 0 if min_index == None else prices[min_index]
#         max_price = 0 if max_index == None else prices[max_index]

#         isBetterMin = True if price < min_price else False
#         isBetterMax = True if price >= max_price else False

#         # min not initialised
#         if min_index == None:
#             min_index = idx
#         elif isBetterMin and (max_index == None or idx < max_index):
#             min_index = idx
#         elif isBetterMax and idx > min_index:
#             max_index = idx
#         elif isBetterMin and idx > max_index:
#             # reset
#             best_cost = max(best_cost, max_price - min_price)
#             min_index = idx
#             max_index = None
#     if max_index != None:  # another was found after the reset
#         best_cost = max(best_cost, prices[max_index] - prices[min_index])
#     return best_cost


def maxProfit(prices: List[int]) -> int:
    l_min_idx, total = 0, 0
    r_max_idx = 1
    while r_max_idx < len(prices):
        if prices[r_max_idx] > prices[l_min_idx]:
            total = max(total, prices[r_max_idx] - prices[l_min_idx])
        else:
            # swap the indexes if they are less
            l_min_idx = r_max_idx
        r_max_idx += 1
    return total


assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert maxProfit([7, 6, 4, 3, 1]) == 0
assert maxProfit([7]) == 0
assert maxProfit([2, 4, 1, 4, 0, 4]) == 4
assert maxProfit([2, 4, 1]) == 2
