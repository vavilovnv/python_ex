"""
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

Category - Medium

You are given an array of strings arr. A string s is formed by the
concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting
some or no elements without changing the order of the remaining elements.
"""

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res, lst = 0, [""]
        for s in arr:
            for word in lst:
                result_word = word + s
                if len(result_word) == len(set(result_word)):
                    lst.append(result_word)
                    res = max(res, len(result_word))
        return res
