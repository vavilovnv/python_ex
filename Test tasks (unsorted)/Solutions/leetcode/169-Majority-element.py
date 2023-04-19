"""
https://leetcode.com/problems/majority-element/

Category - Easy

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, res = 0, nums[0]
        for num in nums:
            if num == res:
                count += 1
            elif count == 0:
                count, res = 0, num
            else:
                count -= 1
        return res    
