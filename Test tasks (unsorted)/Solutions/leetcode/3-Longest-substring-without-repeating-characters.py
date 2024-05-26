"""
https://leetcode.com/problems/reverse-integer/

Category - Medium

Given a string s, find the length of the longest substring without repeating
characters.
"""

# TC O(n), SC O(n) 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = left = 0
        seen, ind = set(), {}
        for right, symbol in enumerate(s):
            if symbol in seen:
                if ind[symbol] < left:
                    res = max(res, right - left + 1)
                else:
                    left = ind[symbol] + 1    
            else:
                res = max(res, right - left + 1)
            seen.add(symbol)
            ind[symbol] = right
        return res
