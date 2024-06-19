"""
https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

Category - Medium

You are given a 0-indexed integer array candies. Each element in the array
denotes a pile of candies of size candies[i]. You can divide each pile into
any number of sub piles, but you cannot merge two piles together.

You are also given an integer k. You should allocate piles of candies to k
children such that each child gets the same number of candies. Each child can
take at most one pile of candies and some piles of candies may go unused.

Return the maximum number of candies each child can get.
"""

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        res, left, right = 0, 1, max(candies)
        while left <= right:
            mid = left + (right - left) // 2
            tmp_k = sum([pile // mid for pile in candies])
            if tmp_k >= k:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res
