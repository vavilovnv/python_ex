"""
https://leetcode.com/problems/kth-largest-element-in-an-array/

Category - Medium

Given an integer array nums and an integer k, return the kth largest element
in the array.

Note that it is the kth largest element in the sorted order, not the kth
distinct element.

Can you solve it without sorting?
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = None
        if not nums or not k or k < 0:
            return res
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        for _ in range(k):
            res = -heapq.heappop(heap)
        return res
