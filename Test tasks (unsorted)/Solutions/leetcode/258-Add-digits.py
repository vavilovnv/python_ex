"""
https://leetcode.com/problems/add-digits/

Category - Easy

Given an integer num, repeatedly add all its digits until the result has only
one digit, and return it.
"""

# TC: O(n)
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = sum(map(int,str(num)))
        return num
    
# TC: O(n)
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            temp, res = num, 0
            while temp > 0:
                res += temp % 10
                temp //= 10
            num = res
        return num
    
# TC: O(1)
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return num % 9 if num % 9 != 0 else 9
