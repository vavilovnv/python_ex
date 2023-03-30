"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/

Category - Easy

Given a string s, reverse the order of characters in each word within a
sentence while still preserving whitespace and initial word order.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        res, lst = [], s.split()
        for word in lst:
            res.append(word[::-1])
        return ' '.join(res)
      