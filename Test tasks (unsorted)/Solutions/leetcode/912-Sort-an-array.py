"""
https://leetcode.com/problems/sort-an-array/

Category - Medium

Given an array of integers nums, sort the array in ascending order and return
it.

You must solve the problem without using any built-in functions in O(nlog(n))
time complexity and with the smallest space complexity possible.
"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sorted(left, right, nums):
            i = j = x = 0
            while i < len(right) and j < len(left):
                if right[i] < left[j]:
                    nums[x] = right[i]
                    i += 1
                else:
                    nums[x] = left[j]
                    j += 1
                x += 1
            nums[x:] = right[i:] if i < len(right) else left[j:]

        def merge_sort(nums):
            if len(nums) == 1:
                return

            mid = len(nums) // 2
            left, right = nums[:mid], nums[mid:]

            merge_sort(left)
            merge_sort(right)

            merge_sorted(left, right, nums)    

        merge_sort(nums)
        return nums
