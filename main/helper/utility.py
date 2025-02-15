from enum import Enum


class StartingCharacter:
    ASCII_START = '\0'
    LOWERCASE_A = 'a'
    UPPERCASE_A = 'A'
    TOTAL_ALPHABET_LOWER_COUNT = 26
    TOTAL_ASCII_COUNT = 128


class getCharacterIndex:
    def __init__(self, starting_character=StartingCharacter.ASCII_START,
                 hash_table_rows=StartingCharacter.TOTAL_ASCII_COUNT,
                 hash_table_columns=1):
        self.starting_char = starting_character
        self.hash_table = [
            [0 for _ in range(hash_table_columns)] for _ in range(hash_table_rows)]

    def get_index(self, character):
        return ord(character) - ord(self.starting_char)

    def get_char(self, idx):
        return chr(idx + ord(self.starting_char))

    def set_value(self, character, value, idx=0):
        self.hash_table[self.get_index(character)][idx] = value

    def increase_value(self, character, value=1, idx=0):
        self.hash_table[self.get_index(character)][idx] += value

    def decrease_value(self, character, value=1, idx=0):
        self.hash_table[self.get_index(character)][idx] -= value

    def get_value(self, character, idx=0):
        return self.hash_table[self.get_index(character)][idx]

    def print(self):
        return {self.get_char(idx): v for idx, v in enumerate(self.hash_table)}
