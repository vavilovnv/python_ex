"""
https://leetcode.com/problems/top-k-frequent-elements/

Category - Medium

Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res, counts, freq = [], Counter(nums), [[] for _ in range(len(nums) + 1)]

        for num, count in counts.items():
            freq[count].append(num)

        for i in range(len(freq)-1, 0, -1):
            res.extend(freq[i])
            if len(res) >= k:
                break

        return res[:k]
