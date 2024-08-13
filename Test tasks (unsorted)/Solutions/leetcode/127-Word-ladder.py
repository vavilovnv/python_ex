"""
https://leetcode.com/problems/word-ladder/

Category - Hard

A transformation sequence from word beginWord to word endWord using a
dictionary wordList is a sequence of words 
beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to
be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the
number of words in the shortest transformation sequence from beginWord to
endWord, or 0 if no such sequence exists. 
"""

from collections import deque
from string import ascii_lowercase

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res, word_set = 0, set(wordList)
        if endWord not in word_set:
            return res

        check_words = deque([beginWord])
        while check_words:
            res += 1
            for _ in range(len(check_words)):
                chars = list(check_words.popleft())
                for i, c in enumerate(chars):
                    for letter in ascii_lowercase:
                        chars[i] = letter
                        w = "".join(chars)
                        if w == endWord:
                            return res + 1
                        if w in word_set:
                            check_words.append(w)
                            word_set.remove(w) 
                        chars[i] = c
        return 0
