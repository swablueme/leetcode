

from helper.utility import visualise_array_slice


def expand(palindrome_centre_idx: tuple, string):
    palindrome_start_idx, palindrome_end_idx = None, None
    max_palindrome = ""

    if len(palindrome_centre_idx) == 1:
        palindrome_start_idx, palindrome_end_idx = palindrome_centre_idx[
            0], palindrome_centre_idx[0]

    elif len(palindrome_centre_idx) == 2:
        palindrome_start_idx, palindrome_end_idx = palindrome_centre_idx[
            0], palindrome_centre_idx[1]

    while palindrome_start_idx >= 0 and palindrome_end_idx <= len(string) - 1:
        if string[palindrome_start_idx] == string[palindrome_end_idx]:
            if palindrome_start_idx == palindrome_end_idx:
                max_palindrome = string[palindrome_start_idx]
            else:
                max_palindrome = string[palindrome_start_idx] + \
                    max_palindrome + string[palindrome_end_idx]
            palindrome_start_idx -= 1
            palindrome_end_idx += 1
        else:
            break
    return max_palindrome


def longestPalindrome(s: str) -> str:
    max_length = ""
    prev_char = None
    for palindrome_centre_idx, character in enumerate(s):
        found_palindrome = expand(
            (palindrome_centre_idx, ), s
        )
        if len(found_palindrome) > len(max_length):
            max_length = found_palindrome

        # if the previous character is the same, it could be part of an even palindrome
        if prev_char == character:
            found_palindrome = expand(
                (palindrome_centre_idx - 1, palindrome_centre_idx), s)
            if len(found_palindrome) > len(max_length):
                max_length = found_palindrome
        prev_char = character
    return max_length


assert longestPalindrome("abc") == "a"
assert longestPalindrome("0") == "0"
assert longestPalindrome("a") == "a"
assert longestPalindrome("aba") == "aba"
assert longestPalindrome("abb") == "bb"
assert longestPalindrome("abba") == "abba"
assert longestPalindrome("facbcad") == "acbca"
assert longestPalindrome("facaaaa") == "aaaa"
