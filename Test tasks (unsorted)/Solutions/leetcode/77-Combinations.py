"""
https://leetcode.com/problems/combinations/

Category - Medium

Given two integers n and k, return all possible combinations of k numbers
chosen from the range [1, n].

You may return the answer in any order.
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(first = 1, curr = []):
            if len(curr) == k:
                res.append(curr[:])
                return
            for i in range(first, n+1):
                curr.append(i)
                helper(i+1, curr)
                curr.pop()
        res = []
        helper()
        return res

"""
hint
use backtracking
"""
