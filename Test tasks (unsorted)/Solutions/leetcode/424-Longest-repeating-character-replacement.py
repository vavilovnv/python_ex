"""
https://leetcode.com/problems/longest-repeating-character-replacement/

Category - Medium

You are given a string s and an integer k. You can choose any character of the
string and change it to any other uppercase English character. You can perform
this operation at most k times.

Return the length of the longest substring containing the same letter you can
get after performing the above operations.
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res, d = 0, {}
        count = start = 0
        for end in range(len(s)):
            d[s[end]] = d.get(s[end], 0) + 1
            count = max(count, d[s[end]])
            if end - start + 1 > count + k:
                d[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
        return res
        