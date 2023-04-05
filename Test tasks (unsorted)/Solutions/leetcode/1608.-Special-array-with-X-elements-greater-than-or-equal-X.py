"""
https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

Category - Easy

You are given an array nums of non-negative integers. nums is considered
special if there exists a number x such that there are exactly x numbers in
nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that
if nums is special, the value for x is unique.
"""

class Solution:
    def specialArray(self, nums: List[int]) -> int:
      nums.sort()
      left, right = 0, len(nums) - 1
      while left <= right:
          mid = left + (right - left)
          x = len(nums) - mid
          if nums[mid] >= x:
              if mid == 0 or nums[mid-1] < x:
                  return x
              else:
                  right = mid - 1
          else:
              left = mid + 1
      return -1

"""
hint
sort and BS. x = len(nums) - mid
""
