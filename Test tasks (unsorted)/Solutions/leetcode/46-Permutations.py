"""
https://leetcode.com/problems/permutations/

Category - Medium

Given an array nums of distinct integers, return all the possible
permutations. You can return the answer in any order.
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(temp = []):
            if len(temp) == len(nums):
                res.append([i for i in temp])
            else:
                for n in nums:
                    if n not in temp:
                        temp.append(n)
                        helper(temp)
                        temp.pop()
        res = []
        helper()
        return res

"""
hint:
use backtracking
"""
