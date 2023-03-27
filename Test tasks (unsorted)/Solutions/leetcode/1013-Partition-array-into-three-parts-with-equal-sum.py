"""
https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/

Category - Easy

Given an array of integers arr, return true if we can partition the array into
three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with
(arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1]
== arr[j] + arr[j + 1] + ... + arr[arr.length - 1])
"""

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sum_arr = sum(arr)
        if sum_arr % 3 != 0:
            return False
        count, temp, target = 0, 0, sum_arr // 3
        for i in arr:
            temp += i
            if temp == target:
                count += 1
                temp = 0
        return count >= 3

"""
hint
Add up and divide by three
""
