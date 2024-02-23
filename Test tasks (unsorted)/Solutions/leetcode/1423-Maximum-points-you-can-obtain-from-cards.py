"""
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

Category - Medium

There are several cards arranged in a row, and each card has an associated
number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the
row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score
you can obtain.
"""

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length, total = len(cardPoints) - k, sum(cardPoints)
        sum_sub = sum(cardPoints[:length])
        res = total - sum_sub
        for i in range(1, len(cardPoints) - length + 1):
            sum_sub = sum_sub - cardPoints[i - 1]  + cardPoints[i + length - 1]
            res = max(res, total - sum_sub)
        return res
