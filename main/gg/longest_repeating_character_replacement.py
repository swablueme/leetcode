# https://www.youtube.com/watch?v=gqXU1UyA8pk

def get_index(character):
    return ord(character) - ord('A')


def get_char(idx):
    return chr(idx + ord('A'))


def is_invalid_window(window_end_idx, window_start_idx, hashtable, number_replacements_allowed):
    array_length = window_end_idx - window_start_idx + 1
    most_freq = max(hashtable)
    return array_length - most_freq > number_replacements_allowed


def characterReplacement(s: str, allowed_replacements: int) -> int:
    current_largest = 0
    window_start_idx, window_end_idx = 0, 0
    hashtable_for_each_character = [0 for idx in range(26)]

    for window_end_idx in range(len(s)):
        array = s[window_start_idx: window_end_idx]

        character = get_index(s[window_end_idx])
        hashtable_for_each_character[character] += 1

        if is_invalid_window(window_end_idx, window_start_idx, hashtable_for_each_character, allowed_replacements) == False:
            current_largest = max(
                window_end_idx - window_start_idx + 1, current_largest)
        else:
            while is_invalid_window(window_end_idx, window_start_idx, hashtable_for_each_character, allowed_replacements) == True:
                # character to remove
                character = get_index(s[window_start_idx])
                # decrease the hashtablet then re-evaluate
                hashtable_for_each_character[character] -= 1
                # increment the start to remove the character
                window_start_idx += 1

            current_largest = max(
                window_end_idx - window_start_idx + 1, current_largest)
    return current_largest


assert characterReplacement("AAABABB", 1) == 5
assert characterReplacement("ABAB", 2) == 4
assert characterReplacement("", 1) == 0
assert characterReplacement(
    "SDSSMESSTR", 2) == 6
assert characterReplacement("ABB", 2) == 3
assert characterReplacement("XYYX", 2) == 4
