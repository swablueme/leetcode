from helper.utility import CharacterHashTable


def makeHashset(word):
    word_hashtable = CharacterHashTable()
    for character in word:
        word_hashtable.increase_value(character)
    return word_hashtable.get_hashable()


def checkInclusion(needle: str, string: str) -> bool:
    if len(string) < len(needle) or len(needle) == 0:
        return False
    needle_to_search = makeHashset(needle)

    needle_start_idx = 0
    needle_end_idx = len(needle) - 1

    word_hashset = CharacterHashTable()
    for character in string[needle_start_idx:needle_end_idx + 1]:
        word_hashset.increase_value(character)

    while True:
        if needle_to_search == word_hashset.get_hashable():
            return True
        word_hashset.decrease_value(string[needle_start_idx])
        needle_start_idx += 1
        needle_end_idx += 1
        if needle_end_idx == len(string):
            break
        word_hashset.increase_value(string[needle_end_idx])
    return False


assert checkInclusion("abc", "cabee") == True
assert checkInclusion("abc", "lecabee") == True
assert checkInclusion("abc", "lecebca") == True
assert checkInclusion("", "lecebca") == False
assert checkInclusion("abc", "le") == False
assert checkInclusion("abc", "") == False
assert checkInclusion("abc", "lelelecb") == False
