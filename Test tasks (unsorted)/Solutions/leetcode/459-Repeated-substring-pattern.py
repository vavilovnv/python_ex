"""
https://leetcode.com/problems/repeated-substring-pattern/

Category - Easy

Given a string s, check if it can be constructed by taking a substring of it
and appending multiple copies of the substring together.
"""

# TC: O(1)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in "".join((s[1:], s[:-1]))
    
# TC: O(1)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)):
            if not s.replace(s[:i], ""):
                return True
        return False
        