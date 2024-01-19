"""
https://leetcode.com/problems/largest-perimeter-triangle/

Category - Easy

Given an integer array nums, return the largest perimeter of a triangle with a
non-zero area, formed from three of these lengths. If it is impossible to form
any triangle of a non-zero area, return 0.
"""

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if sum(nums[i:i + 3]) > 2 * nums[i]:
                return sum(nums[i:i + 3])
        return 0
