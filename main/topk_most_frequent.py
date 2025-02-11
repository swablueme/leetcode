

from collections import Counter
from typing import List

# not optimal - use bucket sort


def topKFrequent(nums: List[int], k: int) -> List[int]:
    return [k[0] for k in Counter(nums).most_common(k)]


print(topKFrequent([1, 2, 2, 3, 3, 3], 2))
print(topKFrequent([7, 7], 1))
