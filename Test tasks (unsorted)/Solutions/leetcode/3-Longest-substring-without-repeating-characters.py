"""
https://leetcode.com/problems/reverse-integer/

Category - Medium

Given a string s, find the length of the longest substring without repeating
characters.
"""

# O(n^2) solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            temp, seek = 0, set()
            for symbol in s[i:]:
                if symbol not in seek:
                    temp += 1
                    res = max(res, temp)
                    seek.add(symbol)
                else:
                    break
        return res

# O(n) solution 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, seen, max_i = 0, {}, 0
        for i in range(len(s)):
            if s[i] not in seen:
                res = max(res, i - max_i + 1)
            else:
                if seen[s[i]] < max_i:
                    res = max(res, i - max_i + 1)
                else:
                    max_i = seen[s[i]] + 1
            seen[s[i]] = i
        return res

"""
hints
use the sliding window to solve the O(n) problem and dict for the items viewed
"""
