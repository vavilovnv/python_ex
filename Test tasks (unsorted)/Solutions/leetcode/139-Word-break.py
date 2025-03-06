"""
https://leetcode.com/problems/word-break/

Category - Medium

Given a string s and a dictionary of strings wordDict, return true if s can be
segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the
segmentation.
"""

# recursive solution
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

# DP solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        words_set = set(wordDict)
        for i in range(len(s) - 1, -1, -1):
            for w in words_set:
                if (i + len(w) <= len(s)) and s[i: i + len(w)] in words_set:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
