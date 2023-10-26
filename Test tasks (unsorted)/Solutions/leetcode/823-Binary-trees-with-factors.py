"""
https://leetcode.com/problems/binary-trees-with-factors/

Category - Medium

Given an array of unique integers, arr, where each integer arr[i] is strictly
greater than 1.

We make a binary tree using these integers, and each number may be used for
any number of times. Each non-leaf node's value should be equal to the product
of the values of its children.

Return the number of binary trees we can make. The answer may be too large so
return the answer modulo 10^9 + 7.
"""

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        d = Counter(arr)
        for i in range(1, len(arr)):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    t = arr[i] // arr[j]
                    if t in arr:
                        d[arr[i]] += d[arr[j]] * d[t]
        return sum(d.values()) % (10**9 + 7)
