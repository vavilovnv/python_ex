"""
https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

Category - Medium

You are given an integer n indicating there are n specialty retail stores.
There are m product types of varying amounts, which are given as a 0-indexed
integer array quantities, where quantities[i] represents the number of
products of the ith product type.

You need to distribute all products to the retail stores following these
rules:
- A store can only be given at most one product type but can be given any
amount of it.
- After distribution, each store will have been given some number of products
(possibly 0). Let x represent the maximum number of products given to any
store. You want x to be as small as possible, i.e., you want to minimize the
maximum number of products that are given to any store.
Return the minimum possible x.
"""

from math import ceil

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 1, max(quantities)
        while left <= right:
            mid = left + (right - left) // 2
            tmp_n = sum([ceil(q / mid) for q in quantities])
            if tmp_n <= n:
                right = mid - 1
            else:
                left = mid + 1
        return left
