"""
https://leetcode.com/problems/longest-string-chain/

Category - Medium

You are given an array of words where each word consists of lowercase English
letters.

wordA is a predecessor of wordB if and only if we can insert exactly one
letter anywhere in wordA without changing the order of the other characters to
make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a
predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1,
where word1 is a predecessor of word2, word2 is a predecessor of word3, and so
on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from
the given list of words.
"""

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        res, d = 1, {}
        for word in sorted(words, key=len):
            d[word] = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in d:
                    d[word] = max(d[word], d[predecessor] + 1)
            res = max(res, d[word])
        return res
