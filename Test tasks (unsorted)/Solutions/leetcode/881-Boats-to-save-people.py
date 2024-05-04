"""
https://leetcode.com/problems/boats-to-save-people/

Category - Medium

You are given an array people where people[i] is the weight of the ith person,
and an infinite number of boats where each boat can carry a maximum weight of
limit. Each boat carries at most two people at the same time, provided the sum
of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res, left, right = 0, 0, len(people) - 1
        while left <= right:
            if people[right] + people[left] <= limit:
                left += 1
            res += 1
            right -= 1
        return res
