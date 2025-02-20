from enum import Enum


class StartingCharacter:
    ASCII_START = '\0'
    LOWERCASE_A = 'a'
    UPPERCASE_A = 'A'
    TOTAL_ALPHABET_LOWER_COUNT = 26
    TOTAL_ASCII_COUNT = 128


def generate_hash_table(number_columns, number_rows):
    if number_columns > 1:
        return [
            [0 for _ in range(number_columns)] for _ in range(number_rows)]
    else:
        return [0 for _ in range(number_rows)]


class CharacterHashTable:
    def __init__(self, starting_character=StartingCharacter.LOWERCASE_A,
                 hash_table_rows=StartingCharacter.TOTAL_ALPHABET_LOWER_COUNT,
                 hash_table_columns=1):
        self.starting_char = starting_character
        self.hash_table = generate_hash_table(
            hash_table_columns, hash_table_rows)
        self.number_columns = hash_table_columns

    def get_index(self, character):
        return ord(character) - ord(self.starting_char)

    def get_char(self, idx):
        return chr(idx + ord(self.starting_char))

    def _get_hashtable_coordinate(self, character, idx):
        if self.number_columns > 1:
            return self.hash_table[self.get_index(character)]
        elif idx == 0:
            return self.hash_table
        else:
            raise Exception(
                f"Single column hashtable doesn't possesss column index {idx}!")

    def set_value(self, character, value, idx=0):
        if self.number_columns > 1:
            self._get_hashtable_coordinate(
                character, idx).__setitem__(idx, value)
        else:
            self._get_hashtable_coordinate(
                character, idx).__setitem__(self.get_index(character), value)

    def increase_value(self, character, value=1, idx=0):
        updated_value = self.get_value(character, idx) + value
        self.set_value(character, updated_value, idx)

    def decrease_value(self, character, value=1, idx=0):
        updated_value = self.get_value(character, idx) - value
        self.set_value(character, updated_value, idx)

    def get_value(self, character, idx=0):
        if self.number_columns > 1:
            return self._get_hashtable_coordinate(character, idx).__getitem__(idx)
        else:
            return self._get_hashtable_coordinate(character, idx).__getitem__(self.get_index(character))

    def print(self):
        return {self.get_char(idx): v for idx, v in enumerate(self.hash_table)}

    def get_hashable(self):
        if self.number_columns == 1:
            return tuple(self.hash_table)
        else:
            return tuple(tuple(row) for row in self.hash_table)


def visualise_array_slice(string, start_idx, end_idx):
    array_representation_string = None
    idx_representation_string = [" " for _ in string]
    if type(string) == str:
        array_representation_string = list(string)
    elif type(string) == list:
        array_representation_string = string

    idx_representation_string.insert(start_idx, str(start_idx))
    idx_representation_string.insert(end_idx + 1, str(end_idx))
    array_representation_string.insert(start_idx, "|")
    array_representation_string.insert(end_idx + 1, "|")

    string_array_slice_value = "".join(array_representation_string)
    to_display_slice_idx_value = "".join(idx_representation_string)
    print(f"   {string_array_slice_value:5s}")
    print(f"   {to_display_slice_idx_value:5s}")
