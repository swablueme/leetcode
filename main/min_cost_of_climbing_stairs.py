from typing import List
import functools
import math


def minCostClimbingStairs(cost):
    cost = tuple(cost)

    @functools.lru_cache(maxsize=300)
    def climb(i=0) -> int:
        if i > len(cost) - 1:
            return 0

        return cost[i] + min(climb(i + 1), climb(i + 2))
    return min(climb(0), climb(1))


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


values = [5, 4, 3, 2, 1]
print(list(range(len(values) - 3, -1, -1)))
