"""
https://leetcode.com/problems/maximum-number-of-balloons/

Category - Easy

Given a string text, you want to use the characters of text to form as many
instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of
instances that can be formed.
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        res = float("inf")
        for c in "balon":
            if c in {"l", "o"}:
                res = min(res, (len(text.split(c)) - 1) // 2)
            else:
                res = min(res, len(text.split(c)) - 1)
        return res
