"""
https://leetcode.com/problems/maximum-product-subarray/

Category - Medium

Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        _max = _min = 1
        for num in nums:
            vals = num, num * _min, num * _max
            _max, _min = max(vals), min(vals)
            res = max(res, _max)
        return res
