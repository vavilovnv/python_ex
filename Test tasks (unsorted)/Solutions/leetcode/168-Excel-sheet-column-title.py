"""
https://leetcode.com/problems/excel-sheet-column-title/

Category - Easy

Given an integer columnNumber, return its corresponding column title as it
appears in an Excel sheet.
"""

from string import ascii_uppercase

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s, ind = ascii_uppercase, []
        while columnNumber:
            columnNumber, d = divmod(columnNumber-1, 26)
            ind.append(d)
        return ''.join([s[i] for i in ind[::-1]])
