"""
https://leetcode.com/problems/maximum-subarray/

Category - Medium

Given an integer array nums, find the subarray with the largest sum, and
return its sum.
"""

# TC: O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curr = nums[0], 0
        for num in nums:
            if curr < 0:
                curr = 0
            curr += num
            res = max(res, curr)
        return res

# approach 2
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum, max_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(cur_sum + nums[i],  nums[i])
            max_sum = max(max_sum, cur_sum)
        return max_sum
