"""
https://leetcode.com/problems/maximum-length-of-pair-chain/

Category - Medium

You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and
lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can
be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in
any order.
"""

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        res, b = 1, pairs[0][1]
        for c, d in pairs[1:]:
            if b < c:
                res += 1
                b = d
        return res
