"""
https://leetcode.com/problems/contains-duplicate-ii/

Category - Easy

Given an integer array nums and an integer k, return true if there are two
distinct indices i and j in the array such that nums[i] == nums[j] and
abs(i - j) <= k.
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = {}
        for i, v in enumerate(nums):
            if v in visited and i-visited[v] <= k:
                return True
            visited[v] = i
        return False
