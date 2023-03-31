"""
https://leetcode.com/problems/longest-palindrome/

Category - Easy

Given a string s which consists of lowercase or uppercase letters, return the
length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome
here.
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        odds = 1 if sum(v % 2 for v in d.values()) else 0
        return sum(v // 2 * 2 for v in d.values()) + odds

"""
hint
use dict, count even of all chars, add 1 odd if it exists
"""
