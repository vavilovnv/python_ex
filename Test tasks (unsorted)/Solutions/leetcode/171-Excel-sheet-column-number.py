"""
https://leetcode.com/problems/excel-sheet-column-number/

Category - Easy

Given a string columnTitle that represents the column title as
appears in an Excel sheet, return its corresponding column
number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i, v in enumerate(reversed(columnTitle)):
            res += (ord(v) - 64) * pow(26, i)
        return res
