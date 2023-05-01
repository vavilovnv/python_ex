"""
https://leetcode.com/problems/container-with-most-water/

Category - Medium

You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and
(i, height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
 
"""

# two pointers
# TC: O(n), SC: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, left, right = 0, 0, len(height) - 1
        while left < right:
            res = max(res, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return res
