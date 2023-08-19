"""
https://leetcode.com/problems/number-of-unequal-triplets-in-array/

Category - Easy

You are given a 0-indexed array of positive integers nums. Find the number of
triplets (i, j, k) that meet the following conditions:

0 <= i < j < k < nums.length
nums[i], nums[j], and nums[k] are pairwise distinct.
In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].
Return the number of triplets that meet the conditions.
"""

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        res, d, prev, nxt = 0, Counter(nums), 0, len(nums)
        for _, v in d.items():
            nxt -= v
            res += prev * v * nxt
            prev += v
        return res
