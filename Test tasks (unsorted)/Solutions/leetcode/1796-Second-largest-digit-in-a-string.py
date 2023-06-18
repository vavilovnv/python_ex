"""
https://leetcode.com/problems/second-largest-digit-in-a-string/

Category - Easy

Given an alphanumeric string s, return the second largest numerical digit that
appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and
digits.
"""

# TC: O(nlogn) SC: O(n)
class Solution:
    def secondHighest(self, s: str) -> int:
        res, digits = -1, set()
        for c in s:
            if c.isdigit():
                digits.add(int(c))
        arr = sorted(list(digits), reverse=True)
        return arr[1] if len(arr) > 1 else -1

# TC: O(n) SC: O(n)
class Solution:
    def secondHighest(self, s: str) -> int:
        res, digits = -1, set()
        for c in s:
            if c.isdigit():
                digits.add(int(c))
        len_digits = len(digits)
        if len_digits <= 1:
            return -1
        arr = list(digits)
        if arr[0] > arr[1]:
            m1, m2 = arr[0], arr[1]
        else:
            m1, m2 = arr[1], arr[0]
        for i in range(2, len_digits):
            if arr[i] > m1:
                m1, m2 = arr[i], m1
            elif arr[i] > m2:
                m2 = arr[i]
        return m2
