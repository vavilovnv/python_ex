"""
https://leetcode.com/problems/find-and-replace-pattern/

Category - Medium

Given a list of strings words and a string pattern, return a list of words[i]
that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that
after replacing every letter x in the pattern with p(x), we get the desired
word.

Recall that a permutation of letters is a bijection from letters to letters:
every letter maps to another letter, and no two letters map to the same
letter.
"""

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res, matches, len_pattern = [], {}, len(set(pattern))
        for word in words:
            matches.clear()
            len_word = len(word)
            if len(set(word)) == len_pattern:
                for i, v in enumerate(word):
                    if v in matches and matches[v] != pattern[i]:
                        break
                    if v not in matches:
                        matches[v] = pattern[i]
                    if i == len_word - 1:
                        res.append(word)
        return res
