"""
https://leetcode.com/problems/find-smallest-letter-greater-than-target/

Category - Easy

You are given an array of characters letters that is sorted in non-decreasing
order, and a character target. There are at least two different characters in
letters.

Return the smallest character in letters that is lexicographically greater
than target. If such a character does not exist, return the first character in
letters.
"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if (mid > 0 and letters[mid-1] <= target < letters[mid] 
                or mid == 0 and target < letters[mid]):
                return letters[mid]
            if target < letters[mid]:
                right -= 1
            else:
                left += 1
        return letters[0]

"""
hint
use a binary search and check that mid > 0 before comparing to target
"""
