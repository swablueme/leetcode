"""
Trie (Prefix tree)
------------------
Insert Word: 0(1)
Search Word: 0(1)
Search Prefix: 0(1)
"""


from collections import defaultdict


class TrieNode:
    def __init__(self, value=""):
        self.children = defaultdict(TrieNode)
        self.value = value
        self.is_finished_word = False

    def __str__(self):
        return self.value


class Trie:
    def __init__(self):
        self.node = TrieNode()

    def traverse(self, word):
        current_node = self.node
        for character in word:
            if character not in current_node.children:
                return None
            current_node = current_node.children[character]
        return current_node

    def starts_with(self, prefix):
        return False if self.traverse(prefix) is None else True

    def insert(self, word):
        current_node = self.node
        for character in word:
            current_node = current_node.children[character]
            current_node.value = character
        current_node.is_finished_word = True
        return current_node
