"""
https://leetcode.com/problems/top-k-frequent-elements/

Category - Medium

Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        return [i[0] for i in sorted(d.items(), key=lambda x: -x[1])][:k]
