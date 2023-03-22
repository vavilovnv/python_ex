"""
https://leetcode.com/problems/can-place-flowers/

Category - Easy

You have a long flowerbed in which some of the plots are planted, and some are
not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty
and 1 means not empty, and an integer n, return if n new flowers can be
planted in the flowerbed without violating the no-adjacent-flowers rule.
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        len_f = len(flowerbed) - 1
        for i, v in enumerate(flowerbed):
            if (v == 0
                    and (i == 0 or flowerbed[i-1] == 0)
                    and (i == len_f or flowerbed[i+1] == 0)):
                flowerbed[i] = 1
                n -= 1
            if n == 0:
                return True
        return False

"""
hint
check the borders and neighboring locations. if 0 - plant the flower =)
"""
