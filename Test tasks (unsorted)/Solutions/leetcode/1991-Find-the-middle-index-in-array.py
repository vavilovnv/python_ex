"""
https://leetcode.com/problems/find-the-middle-index-in-array/

Category - Easy

Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e.,
the smallest amongst all the possible ones).

A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1]
== nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

If middleIndex == 0, the left side sum is considered to be 0. Similarly, if
middleIndex == nums.length - 1, the right side sum is considered to be 0.

Return the leftmost middleIndex that satisfies the condition, or -1 if there
is no such index.
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
      temp, sum_nums, len_nums = 0, sum(nums), len(nums) - 1
      for i in range(len_nums):
          sum_nums -= nums[i]
          if sum_nums == temp:
              return i
          temp += nums[i]
      if temp == 0:
          return len_nums
      return -1
            
"""
this problem and problem #724 - the same
"""
