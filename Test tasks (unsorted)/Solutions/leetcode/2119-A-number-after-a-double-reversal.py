"""
https://leetcode.com/problems/a-number-after-a-double-reversal/

Category - Easy

Reversing an integer means to reverse all its digits.

For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the
leading zeros are not retained.
Given an integer num, reverse num to get reversed1, then reverse reversed1 to
get reversed2. Return true if reversed2 equals num. Otherwise return false.
"""

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
         return num == int(str(int(str(num)[::-1]))[::-1])
