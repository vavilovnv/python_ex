"""
https://leetcode.com/problems/longest-palindromic-substring/

Category - Medium

Given a string s, return the longest palindromic substring in s.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len, len_s, res = 0, len(s), ""
        for i in range(len_s):
            for j in range(2):
                left, right = i, i + j
                while (left >= 0) and (right < len_s) and s[left] == s[right]:
                    temp_len = right - left + 1 
                    if temp_len > max_len:
                        max_len, res = temp_len, s[left:right + 1]
                    left -= 1
                    right += 1
        return res
