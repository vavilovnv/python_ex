"""
https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

Category - Easy

You are given an integer array nums. You need to create a 2D array from nums
satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.
"""

# TC: O(n) SC: O(n)
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res, d = [], Counter(nums)
        for num in set(nums):
            counts = d[num]
            for i in range(counts):
                if len(res) <= i:
                    res.append([])
                res[i].append(num)
                d[num] -= 1
        return res
