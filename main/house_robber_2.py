from typing import List


def house_robber_1(nums: List[int]) -> int:
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


def rob(nums: List[int]) -> int:
    if len(nums) <= 3:
        return max(nums)
    return max(house_robber_1(nums[1:]), house_robber_1(nums[:-1]))


assert rob([3]) == 3
assert rob([4]) == 4
assert rob([3, 4, 3]) == 4
assert rob([2, 9, 8, 3, 6]) == 15
assert rob([0, 15, 0, 15]) == 30
assert rob([1, 0, 15, 0, 15]) == 30
assert rob([0, 1, 0, 15, 0, 15]) == 31
