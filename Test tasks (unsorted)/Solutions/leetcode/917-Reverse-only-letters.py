"""
https://leetcode.com/problems/reverse-only-letters/

Category - Easy

Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.
"""

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left, right, arr = 0, len(s) - 1, list(s)
        while left < right:
            if arr[left].isalpha() and arr[right].isalpha():
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            else:
                if not arr[left].isalpha():
                    left += 1
                if not arr[right].isalpha():
                    right -= 1
        return ''.join(arr)    
