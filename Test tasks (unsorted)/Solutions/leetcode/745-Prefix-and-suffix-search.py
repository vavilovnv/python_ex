"""
https://leetcode.com/problems/prefix-and-suffix-search/

Category - Hard

Design a special dictionary that searches the words in it by a prefix and a
suffix.

Implement the WordFilter class:
WordFilter(string[] words) Initializes the object with the words in the
dictionary.
f(string pref, string suff) Returns the index of the word in the dictionary,
which has the prefix pref and the suffix suff. If there is more than one
valid index, return the largest of them. If there is no such word in the
dictionary, return -1.
"""

class WordFilter:

    def __init__(self, words: List[str]):
        self.d = {}
        for i in range(len(words)):
            len_word = len(words[i])
            for j in range(1, min(11, len_word + 1)):
                prfx = words[i][:j]
                if prfx not in self.d:
                    self.d[prfx] = {}
                for _j in range(1, min(11, len_word+1)):
                    sfx = words[i][len_word - _j:]
                    self.d[prfx][sfx] = i

    def f(self, prefix: str, suffix: str) -> int:
        if prefix not in self.d or suffix not in self.d[prefix]:
            return -1
        return self.d[prefix][suffix]
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
