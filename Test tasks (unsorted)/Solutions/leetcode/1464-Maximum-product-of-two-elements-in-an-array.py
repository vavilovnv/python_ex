"""
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

Category - Easy

Given the array of integers nums, you will choose two different indices i and
j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mmx, mx = max(nums[0], nums[1]), min(nums[0], nums[1])
        for num in nums[2:]:
            if num > mmx:
                mx, mmx = mmx, num
            elif num > mx:
                mx = num
        return (mmx - 1) * (mx - 1)
