"""
https://leetcode.com/problems/fair-distribution-of-cookies/

Category - Medium

You are given an integer array cookies, where cookies[i] denotes the number of
cookies in the ith bag. You are also given an integer k that denotes the
number of children to distribute all the bags of cookies to. All the cookies
in the same bag must go to the same child and cannot be split up.

The unfairness of a distribution is defined as the maximum total cookies
obtained by a single child in the distribution.

Return the minimum unfairness of all distributions.
"""

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def helper(i, count):
            if n - i < count:
                return float('inf')
            if i == n:
                return max(bags)
            res = float('inf')
            for j in range(k):
                count -= int(bags[j] == 0)
                bags[j] += cookies[i]
                res = min(res, helper(i + 1, count))
                bags[j] -= cookies[i]
                count += int(bags[j] == 0)
            return res
        
        bags, n = [0] * k, len(cookies)
        return helper(0, k)
