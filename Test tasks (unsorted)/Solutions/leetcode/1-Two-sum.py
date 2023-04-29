"""
https://leetcode.com/problems/two-sum/

Category - Easy

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.
"""

# TC: O(n), SC: memory O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, v in enumerate(nums):
            if v in d:
                return [i, d[v]]
            d[target - v] = i

# TC: O(n), SC: memory O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return([left, right])
            if nums[left] + nums[right] > target:
                if nums[left] < nums[right]:
                    right -= 1
                else:
                    left += 1
            else:
                if nums[left] < nums[right]:
                    left += 1
                else:
                    right -= 1  
