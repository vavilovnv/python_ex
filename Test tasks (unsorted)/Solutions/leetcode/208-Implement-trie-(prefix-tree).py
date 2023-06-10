"""
https://leetcode.com/problems/implement-trie-prefix-tree/

Category - Medium

A trie (pronounced as "try") or prefix tree is a tree data structure used to
efficiently store and retrieve keys in a dataset of strings. There are various
applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie
(i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously
inserted string word that has the prefix prefix, and false otherwise.
"""

class NodeTrie:
    
    def __init__(self):
        self.__children = {}
        self.whole_word = False

    def __contains__(self, value):
        return value in self.__children

    def __getitem__(self, char):
        return self.__children[char]

    def create_sub_trie(self, char):
        self.__children[char] = NodeTrie()

class Trie:

    def __init__(self):
        self.root = NodeTrie()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr:
                curr.create_sub_trie(c)
            curr = curr[c]
        curr.whole_word = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        return curr.whole_word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        return True
