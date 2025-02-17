from typing import List
import functools
import math


def minCostClimbingStairs(cost):
    total_cost = math.inf

    @functools.lru_cache()
    def climb(cost: List[int], i=0, found_total_cost=0) -> int:
        nonlocal total_cost
        if i > len(cost) - 1:
            total_cost = min(total_cost, found_total_cost)
            return

        if i == 0:
            j = 1
            foundCost = cost[j]
            climb(
                cost, j + 1, found_total_cost + foundCost)
            climb(
                cost, j + 2, found_total_cost + foundCost)
        foundCost = cost[i]
        climb(
            cost, i + 1, found_total_cost + foundCost)
        climb(
            cost, i + 2, found_total_cost + foundCost)
    climb(tuple(cost))

    return total_cost


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return minCostClimbingStairs(cost)


assert minCostClimbingStairs([100, 99]) == 99
assert minCostClimbingStairs([1, 2]) == 1
assert minCostClimbingStairs([1, 2, 3]) == 2
assert minCostClimbingStairs([1, 2, 1, 2, 1, 1, 1]) == 4
assert minCostClimbingStairs([10, 15, 20]) == 15
assert minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
# Solution().minCostClimbingStairs([100, 99])
