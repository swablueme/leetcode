from itertools import groupby
from typing import Counter, List
from collections import defaultdict


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    d = defaultdict(list)

    value = groupby(strs, key=lambda x: sorted(x))
    for k, v in value:
        d[tuple(k)].extend(list(v))
    return list(d.values())


print(groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))
