from typing import List


def hasDuplicate(nums: List[int]) -> bool:
    found_values = set()
    for value in nums:
        if value in found_values:
            return True
        else:
            found_values.add(value)
    return False
