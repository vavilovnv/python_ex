"""
https://leetcode.com/problems/combination-sum-iv/

Category - Medium

Given an array of distinct integers nums and a target integer target, return
the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.
"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for i in range(1, target + 1):
            dp[i] = 0
            for num in nums:
                dp[i] += dp.get(i - num, 0)
        return dp[target]
