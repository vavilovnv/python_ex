"""
https://leetcode.com/problems/subsets/

Category - Medium

Given an integer array nums of unique elements, return all possible subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in
any order.
"""

# backtracking solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(start, subset):
            res.append(subset[:])
            for i in range(start, len(nums)):
                subset.append(nums[i])
                helper(i + 1, subset)
                subset.pop()
        res = []
        helper(0, [])
        return res

# iterable solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [subset + [num] for subset in res]
        return res
