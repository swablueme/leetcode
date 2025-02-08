from itertools import groupby
from typing import Counter, List
from collections import defaultdict


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # O(M x NlogN) complexity
    d = defaultdict(list)

    value = groupby(strs, key=lambda x: sorted(x))
    for k, v in value:
        d[tuple(k)].extend(list(v))
    return list(d.values())


def translate_word(word):
    word_array = [0] * 26
    starting_index_characters = ord('a')
    for character in word:
        index = ord(character) - starting_index_characters
        word_array[index] += 1
    return tuple(word_array)


def groupAnagrams2(strs: List[str]) -> List[List[str]]:
    # O(MN) complexity
    d = defaultdict(list)
    [d[translate_word(word)].append(word) for word in strs]
    print(d)
    return d.values()


print(groupAnagrams2(["act", "pots", "tops", "cat", "stop", "hat"]))
print(groupAnagrams2([""]))
print(groupAnagrams2(["a"]))
