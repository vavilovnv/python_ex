"""
https://leetcode.com/problems/word-subsets/

Category - Medium

You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including
multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a
subset of a.

Return an array of all the universal strings in words1. You may return the
answer in any order.
"""

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        result, freq, mx = [], {}, 0
        for word in words2:
            for c in word:
                count = word.count(c)
                if c in freq:
                    if count - freq[c] > 0: 
                        freq[c] = count
                        mx += count - freq[c]
                else: 
                    freq[c] = count
                    mx += count
            if mx > 10: 
                return result
        for word in words1:
            if len(word) >= mx: 
                to_append = True
                for c in freq:
                    if word.count(c) < freq[c]: 
                        to_append = False
                        break
                if to_append: 
                    result.append(word)
        return result
