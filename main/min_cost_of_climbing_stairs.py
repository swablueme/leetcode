from typing import List
import functools
import math


def minCostClimbingStairs(cost):
    cost = tuple(cost)

    @functools.lru_cache(maxsize=300)
    def climb(i=0) -> int:
        if i > len(cost) - 1:
            return 0

        j = 1
        if i == 0:
            return min(cost[j] + min(climb(j + 1), climb(j + 2)), cost[i] + min(climb(i + 1), climb(i + 2)))
        return cost[i] + min(climb(i + 1), climb(i + 2))
    return climb()


# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         return minCostClimbingStairs(cost)


assert minCostClimbingStairs([100, 99]) == 99
assert minCostClimbingStairs([1, 2]) == 1
assert minCostClimbingStairs([1, 2, 3]) == 2
assert minCostClimbingStairs([1, 2, 1, 2, 1, 1, 1]) == 4
assert minCostClimbingStairs([10, 15, 20]) == 15
assert minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
# Solution().minCostClimbingStairs([100, 99])
