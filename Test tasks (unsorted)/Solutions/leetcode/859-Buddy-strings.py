"""
https://leetcode.com/problems/buddy-strings/

Category - Easy

Given two strings s and goal, return true if you can swap two letters in s so
the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such
that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
"""

# TC: O(n) SC: O(n)
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        left, right, s_arr, swaps = 0, len(s) - 1, list(s), 0
        while left < right:
            if s[left] != goal[left] and s[right] != goal[right]:
                s_arr[left], s_arr[right] = s_arr[right], s_arr[left]
                if ''.join(s_arr) == goal:
                    swaps += 1
                    if swaps > 1:
                        return False
                    left += 1
                    right -= 1
                else:
                    return False
            elif s[left] != goal[left]:
                right -= 1
            elif s[right] != goal[right]:
                left += 1
            else:
                left += 1
                right -= 1
        return swaps == 1 or s == goal and len(s) - len(set(s)) > 0
