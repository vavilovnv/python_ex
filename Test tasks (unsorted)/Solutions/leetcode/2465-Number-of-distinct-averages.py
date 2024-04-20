"""
https://leetcode.com/problems/number-of-distinct-averages/

Category - Easy

You are given a 0-indexed integer array nums of even length.

As long as nums is not empty, you must repetitively:
Find the minimum number in nums and remove it.
Find the maximum number in nums and remove it.
Calculate the average of the two removed numbers.
The average of two numbers a and b is (a + b) / 2.

For example, the average of 2 and 3 is (2 + 3) / 2 = 2.5.
Return the number of distinct averages calculated using the above process.

Note that when there is a tie for a minimum or maximum number, any can be
removed.
"""

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        res, i, j = set(), 0, len(nums)-1
        while i <= j:
            res.add((nums[i] + nums[j]) / 2)
            i+=1
            j-=1
        return len(res)
