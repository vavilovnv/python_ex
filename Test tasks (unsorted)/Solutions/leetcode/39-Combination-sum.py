"""
https://leetcode.com/problems/combination-sum/

Category - Medium

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen
numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that
sum up to target is less than 150 combinations for the given input.
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(arr, temp_res, s):
            if s == target:
                res.append(temp_res)
            if s > target:
                return
            for i in range(len(arr)):
                helper(arr[i:], temp_res + [arr[i]], s + arr[i])
        res = []
        helper(candidates, [], 0)
        return res

"""
hint
backtracking
"""
