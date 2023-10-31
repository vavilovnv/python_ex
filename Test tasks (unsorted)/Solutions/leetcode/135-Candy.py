"""
https://leetcode.com/problems/candy/description/

Category - Hard

There are n children standing in a line. Each child is assigned a rating value
given in the integer array ratings.

You are giving candies to these children subjected to the following
requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the
candies to the children.
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        lst = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                lst[i] = lst[i-1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if lst[i] <= lst[i+1] and ratings[i] > ratings[i+1]:
                lst[i] = lst[i+1] + 1
        return sum(lst)
