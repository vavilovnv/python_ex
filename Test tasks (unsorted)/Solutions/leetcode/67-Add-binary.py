"""
https://leetcode.com/problems/add-binary/

Category - Easy

Given two binary strings a and b, return their sum as a binary string.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        arr_a, arr_b = list(a), list(b)
        res, carry = [], False
        while arr_a or arr_b or carry:
            x = arr_a.pop() if arr_a else '0'
            y = arr_b.pop() if arr_b else '0'
            if x == y:
                if carry:
                    res.append('1')
                    carry = False if x == '0' else True
                else:
                    res.append('0')
                    carry = True if x == '1' else False
            else:
                if carry:
                    res.append('0')
                    carry = True
                else:
                    res.append('1')
        return ''.join(res[::-1])
