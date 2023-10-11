"""
https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

Category - Medium

Given an integer array nums of size n, return the minimum number of moves
required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.
"""

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        res, mid = 0, nums[len(nums) // 2]
        for num in nums:
            res += abs(mid - num)
        return res
        