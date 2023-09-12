"""
https://leetcode.com/problems/combination-sum-iv/

Category - Medium

Given an array of distinct integers nums and a target integer target, return
the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.
"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        if target < nums[0]:
            return 0
        lst = [0 for i in range(target+1)]
        for i in range(target, -1, -1):
            for j in nums:
                if i + j > target:
                    break
                if i + j < target:
                    lst[i] = lst[i] + lst[i+j]
                else:
                    lst[i] += 1
        return lst[0]
