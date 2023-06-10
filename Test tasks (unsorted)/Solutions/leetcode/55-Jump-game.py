"""
https://leetcode.com/problems/jump-game/

Category - Medium

You are given an integer array nums. You are initially positioned at the
array's first index, and each element in the array represents your maximum
jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        temp = nums[0]
        for i in range(1, len(nums)):
            if temp == 0:
                return False
            temp = max(temp - 1, nums[i])
        return True
