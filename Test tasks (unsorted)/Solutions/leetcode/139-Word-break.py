"""
https://leetcode.com/problems/word-break/

Category - Medium

Given a string s and a dictionary of strings wordDict, return true if s can be
segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the
segmentation.
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def helper(s):
            if not s:
                return True
            for word in wordDict:
                if s.startswith(word) and helper(s[len(word):]):
                    return True
            return False

        return helper(s)
