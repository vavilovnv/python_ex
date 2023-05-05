"""
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

Category - Medium

Given a string s and an integer k, return the maximum number of vowel letters
in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""

# Sliding window TC: O(n) SC: O(1)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = count = 0
        for i, v in enumerate(s):
            if v in 'aeiou':
                count += 1
            if i >= k and s[i-k] in 'aeiou':
                count -= 1
            res = max(res, count)
        return res
