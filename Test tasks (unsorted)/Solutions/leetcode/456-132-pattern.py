"""
https://leetcode.com/problems/assign-cookies/

Category - Easy

Assume you are an awesome parent and want to give your children some cookies.
But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie
that the child will be content with; and each cookie j has a size s[j]. If
s[j] >= g[i], we can assign the cookie j to the child i, and the child i will
be content. Your goal is to maximize the number of your content children and
output the maximum number.
"""

# TC: O(nlogn)
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = i = 0
        g.sort()
        s, len_g = sorted(s)[::-1], len(g)
        while s and i < len_g:
            if g[i] <= s[-1]:
                res += 1
                i += 1
            s.pop()
        return res
