"""
https://leetcode.com/problems/longest-increasing-subsequence/

Category - Medium

Given an integer array nums, return the length of the longest strictly
increasing subsequence.
"""

#TC: O(n log n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res, tails = 0, [0] * len(nums)
        for num in nums:
            left, right = 0, res
            while left != right:
                mid = left + (right - left) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            res = max(res, left + 1)
            tails[left] = num
        return res
    
#TC: O(n ^ 2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
