"""
https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

Category - Easy

Given a positive integer num represented as a string, return the integer num
without trailing zeros as a string.
"""

# TC: O(n) SC: O(1)
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        count = len(num)
        for i in range(len(num)-1, - 1, -1):
            if num[i] == "0":
                count -= 1
            else:
                break
        return num[:count]

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip("0")
