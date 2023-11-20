"""
https://leetcode.com/problems/matchsticks-to-square/

Category - Medium

You are given an integer array matchsticks where matchsticks[i] is the length
of the ith matchstick. You want to use all the matchsticks to make one square.
You should not break any stick, but you can link them up, and each matchstick
must be used exactly one time.

Return true if you can make this square and false otherwise.
"""

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False
        sides, sum_m, max_m = 4, sum(matchsticks), max(matchsticks)
        if sum_m % sides != 0 or max_m > sum_m // sides:
            return False
        used = [False] * len(matchsticks)
        
        def helper(target, cur, i, sides):
            if sides == 1:
                return True
            if cur == target:
                return helper(target, 0, 0, sides-1)
            for j in range(i, len(matchsticks)):
                if used[j] or cur + matchsticks[j] > target:
                    continue
                used[j] = True
                if helper(target, cur+matchsticks[j], j+1, sides):
                    return True
                used[j] = False
            return False
        return helper(sum_m//sides, 0, 0, sides)
