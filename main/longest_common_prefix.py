import math
from typing import List

from data_structures.trie import Trie


def longestCommonPrefix(strs: List[str]) -> str:
    trie = Trie()
    trie.insert(strs[0])
    prefix_length_common = float('inf')
    for word in strs[1:]:
        current_prefix_length = float(
            '-inf')
        for idx in range(1, len(word) + 1):
            prefix = word[:idx]
            if trie.is_starts_with(prefix):
                current_prefix_length = idx
        prefix_length_common = min(current_prefix_length, prefix_length_common)
    if not math.isinf(prefix_length_common):
        return strs[0][:prefix_length_common]
    if len(strs) == 1:
        return strs[0]
    else:
        return ""


def longestCommonPrefix2(strs: List[str]) -> str:
    prefix_set = set()
    prefix_length_common = len(strs[0])
    for word_number, word in enumerate(strs):
        current_prefix_length = float('-inf')
        for idx in range(1, len(word) + 1):
            prefix = word[:idx]
            if word_number == 0:
                prefix_set.add(prefix)
            else:
                if prefix in prefix_set:
                    current_prefix_length = idx
        if word_number != 0:
            prefix_length_common = min(
                current_prefix_length, prefix_length_common)
    if not math.isinf(prefix_length_common):
        return strs[0][:prefix_length_common]
    else:
        return ""


if __name__ == "__main__":
    print(longestCommonPrefix2(["a"]))
    print(longestCommonPrefix2(["flow", "flow", "flow"]))
    print(longestCommonPrefix2(["flower", "flow", "flight"]))
    print(longestCommonPrefix2(["dog", "racecar", "car"]))
