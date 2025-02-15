from helper.utility import getCharacterIndex


def lengthOfLongestSubstring(string: str) -> int:
    index = getCharacterIndex('\0', 128)
    start_idx, end_idx, total_length = 0, 0, 0
    for idx, character in enumerate(string):
        end_idx = idx
        index.increase_value(character)
        if index.get_value(character) > 1:
            while index.get_value(character) >= 2:
                index.decrease_value(string[start_idx])
                start_idx += 1
        total_length = max(total_length, end_idx - start_idx + 1)
    return total_length


assert lengthOfLongestSubstring("abb") == 2
assert lengthOfLongestSubstring("abbcaccefdgdd") == 5
assert lengthOfLongestSubstring("pwwkew") == 3
assert lengthOfLongestSubstring("a") == 1
assert lengthOfLongestSubstring("aaaaaa") == 1
assert lengthOfLongestSubstring("aaaaaad") == 2
assert lengthOfLongestSubstring("") == 0
assert lengthOfLongestSubstring("zxyzxyz") == 3
