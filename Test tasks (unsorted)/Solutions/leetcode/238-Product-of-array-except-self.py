"""
https://leetcode.com/problems/product-of-array-except-self/

Category - Medium

Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
integer.

You must write an algorithm that runs in O(n) time and without using the
division operation.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        right, left = [1] * (len_nums), [1] * (len_nums)
        for i, v in enumerate(nums[:-1], 1):
            right[i] = right[i-1] * v
        for i, v in enumerate(nums[1:][::-1], 1):
            left[i] =  left[i-1] * v
        return [right[i] * left[len_nums-i-1]  for i, v in enumerate(right)]

"""
hint
mul all elements from -1 to index n-1, mul from n+1 to 1, then the results mul
"""
