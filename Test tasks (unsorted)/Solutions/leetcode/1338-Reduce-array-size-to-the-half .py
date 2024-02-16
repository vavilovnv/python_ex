"""
https://leetcode.com/problems/reduce-array-size-to-the-half/

Category - Medium

You are given an integer array arr. You can choose a set of integers and
remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers
of the array are removed.
"""

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        res, half = 0, len(arr) // 2
        num_counts = Counter(arr)
        num_freq = sorted(num_counts.values(), reverse=True)
        while half > 0:
            half -= num_freq[res]
            res += 1
        return res
