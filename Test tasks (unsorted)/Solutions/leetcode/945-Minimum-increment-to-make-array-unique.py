"""
https://leetcode.com/problems/valid-mountain-array/

Category - Medium

You are given an integer array nums. In one move, you can pick an index i
where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.
"""

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        res, freq = 0, [0] * (len(nums) + max(nums) + 1)
        for num in nums:
            freq[num] += 1
        for i in range(len(freq)):
            if freq[i] <= 1:
                continue
            duplicates = freq[i] - 1
            freq[i] = 1
            freq[i + 1] += duplicates
            res += duplicates
        return res