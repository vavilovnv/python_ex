"""
https://leetcode.com/problems/palindrome-number/

Category - Easy

Given an integer x, return true if x is a palindrome, and false otherwise.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
