"""
https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

Category - Medium

You are given an integer array nums.

In one move, you can choose one element of nums and change it to any value.

Return the minimum difference between the largest and smallest value of nums
after performing at most three moves.
"""

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort(reverse=True)
        res, a, b = float('inf'), nums[:4], nums[-4:]
        return min(a[i] - b[i] for i in range(4))
