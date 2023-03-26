"""
https://leetcode.com/problems/count-primes/

Category - Medium

Given an integer n, return the number of prime numbers that are strictly less
than n.
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        nums = list(range(n))
        for i in range(int(n ** 0.5) + 1):
            if i < 2:
                nums[i] = 0
            if nums[i] > 0:
                for j in range(i * i, n, i):
                    nums[j] = 0
        return len(set(nums))-1

"""
hints
1. Use Sieve of Eratosthenes
2. In the first loop, take the range up to the root of n
"""
