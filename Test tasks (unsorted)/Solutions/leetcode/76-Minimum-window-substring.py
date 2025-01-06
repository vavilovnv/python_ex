"""
https://leetcode.com/problems/minimum-window-substring/

Category - Hard

Given two strings s and t of lengths m and n respectively, return the minimum
window 
substring
 of s such that every character in t (including duplicates) is included in the
 window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""

from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res, need = [], Counter(t)
        need_length = len(need)
        window, window_length = defaultdict(int), float("inf")
        left = have_length = 0
        for right, c in enumerate(s):
            window[c] += 1
            if c in need and window[c] == need[c]:
                have_length += 1

            while have_length == need_length:
                if (right - left + 1) < window_length:
                    res = [left, right]
                    window_length = right - left + 1

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have_length -= 1
                left += 1

        return "" if not res else s[res[0]:res[1] + 1]
