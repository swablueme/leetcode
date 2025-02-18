

from typing import List


def rob(nums: List[int]) -> int:
    cost = [0 for _ in nums]

    for idx, number in enumerate(nums):
        curr_cost = 0
        if idx <= 1:
            cost[idx] = number
        else:
            curr_cost = max(
                number + max(cost[idx - 2], cost[idx - 3]), curr_cost)
            cost[idx] = curr_cost

    return max(cost)


assert rob([2, 1, 1, 2]) == 4
assert rob([99, 100]) == 100
assert rob([100]) == 100
assert rob([0]) == 0
assert rob([1, 1, 3, 3]) == 4
assert rob([2, 9, 8, 3, 6]) == 16

assert rob([1, 2, 3, 1]) == 4
assert rob([2, 7, 9, 3, 1]) == 12
