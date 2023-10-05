"""
https://leetcode.com/problems/majority-element-ii/

Category - Medium

Given an integer array of size n, find all elements that appear more than
⌊ n/3 ⌋ times.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d, n = Counter(nums), len(nums) / 3
        return [k for k, v in d.items() if v > n]
