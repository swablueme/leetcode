from typing import List
from collections import defaultdict


def twoSum(nums: List[int], target: int) -> List[int]:
    d = defaultdict(list)

    for idx, number in enumerate(nums):
        diff_from_target = target - number
        if diff_from_target in d:
            return list(sorted([idx, d[diff_from_target][0]]))
        d[number].append(idx)

    # for number in d:
    #     diff_from_target = target - number
    #     if diff_from_target in d:
    #         if diff_from_target == number and len(d[number]) > 1:
    #             return [d[number][0], d[number][1]]
    #         elif diff_from_target != number:
    #             return list(sorted([d[diff_from_target][0], d[number][0]]))


"""
    # # sorted
    # index_i, index_j = [0, len(nums) - 1]
    # nums = list(sorted(nums))

    # while True:
    #     left_num = nums[index_i]
    #     right_num = nums[index_j]
    #     if left_num + right_num == target:
    #         return [index_i, index_j]
    #     elif left_num + right_num < target:
    #         index_i += 1
    #     else:
    #         index_j -= 1

"""
# twoSum([3, 4, 5, 6], 7)
# twoSum([4, 5, 6], 10)
# twoSum([5, 5], 10)
# print(twoSum([3, 2, 3], 6))
