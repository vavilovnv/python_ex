"""
https://leetcode.com/problems/pascals-triangle/

Category - Easy

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above
it.
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows-1):
            temp = [0] + res[-1] + [0]
            res.append([temp[i] + temp[i-1] for i in range(1, len(temp))])
        return res

"""
hint
At each step of loop use [0] + res[-1] + [0] and add in the loop i and i-1
res element
"""
