"""
https://leetcode.com/problems/max-consecutive-ones-iii/

Category - Easy

Given a binary array nums and an integer k, return the maximum number of
consecutive 1's in the array if you can flip at most k 0's.
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = left = right = 0
        for right, value in enumerate(nums):
            zeros += value == 0
            if zeros > k:
                zeros -= nums[left] == 0
                left += 1
        return right - left + 1

# patterns 
# task 485 (https://leetcode.com/problems/max-consecutive-ones/) the same (approach 2)