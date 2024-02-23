"""
https://leetcode.com/problems/construct-target-array-with-multiple-sums/

Category - Hard

You are given an array target of n integers. From a starting array arr
consisting of n 1's, you may perform the following procedure :
- let x be the sum of all elements currently in your array.
- choose index i, such that 0 <= i < n and set the value of arr at index i to
x.
- You may repeat this procedure as many times as needed.

Return true if it is possible to construct the target array from arr,
otherwise, return false.
"""

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1
        total, heap = sum(target), []
        for i in target:
            heappush(heap, -i)
        while True:
            i = -heappop(heap)
            delta = total - i
            if i == 1 or delta == 1: 
                return True
            if delta != 0:
                if i % delta == i or i % delta == 0: 
                    return False
                i = i % delta
            heappush(heap, -i)
            total = i + delta
