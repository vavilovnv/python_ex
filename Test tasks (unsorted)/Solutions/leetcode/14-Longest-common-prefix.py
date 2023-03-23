"""
https://leetcode.com/problems/longest-common-prefix/

Category - Easy

Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string "".
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for i in range(len(min(strs, key=len))):
            symbol = strs[0][i]
            if not all([s[i] == symbol for s in strs]):
                break
            prefix += symbol
        return prefix
