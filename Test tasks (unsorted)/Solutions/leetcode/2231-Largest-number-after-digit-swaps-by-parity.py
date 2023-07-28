"""
https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

Category - Easy

You are given a positive integer num. You may swap any two digits of num that
have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.
"""

# TC: O(nlogn) SC: O(n)
class Solution:
    def largestInteger(self, num: int) -> int:
        arr, res = list(map(int, list(str(num)))), 0
        evens = sorted(x for x in arr if x % 2 == 0)
        odds = sorted(x for x in arr if x % 2 == 1)
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                res = res*10 + evens.pop()
            else:
                res = res*10 + odds.pop()
        return res
