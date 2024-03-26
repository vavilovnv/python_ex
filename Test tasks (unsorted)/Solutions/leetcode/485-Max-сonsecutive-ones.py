"""
https://leetcode.com/problems/max-consecutive-ones/

Category - Easy

Given a binary array nums, return the maximum number of consecutive 1's in the
array.
"""

# Approach 1
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, count = 0, 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                res = max(res, count)
                count = 0
        res = max(res, count)
        return res
        
# Approach 2
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zeros, l = 0, 0
        for r, n in enumerate(nums):
            zeros += n == 0
            if zeros > 0: # the difference is only here
                zeros -= nums[l] == 0
                l += 1
        return r - l + 1
