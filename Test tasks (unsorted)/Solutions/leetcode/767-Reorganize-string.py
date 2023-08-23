"""
https://leetcode.com/problems/reorganize-string/

Category - Medium

Given a string s, rearrange the characters of s so that any two adjacent
characters are not the same.

Return any possible rearrangement of s or return "" if not possible.
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        res, d = [], Counter(s)
        heap = [(-v, k) for k, v in d.items()]
        heapq.heapify(heap)
        while(len(heap) > 1):
            a, b = heapq.heappop(heap), heapq.heappop(heap)
            res.extend([a[1], b[1]])
            if a[0] < -1:
                heapq.heappush(heap, (a[0] + 1, a[1]))
            if b[0] < -1:
                heapq.heappush(heap, (b[0] + 1, b[1]))
        if heap:
            if heap[0][0] < -1:
                return ""
            res.append(heap[0][1])
        return "".join(res)
