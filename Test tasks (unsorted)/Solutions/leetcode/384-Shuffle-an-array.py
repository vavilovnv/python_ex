"""
https://leetcode.com/problems/shuffle-an-array/

Category - Medium

Given an integer array nums, design an algorithm to randomly shuffle the
array. All permutations of the array should be equally likely as a result of
the shuffling.

Implement the Solution class:
Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.
"""

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.stored = nums[:]

    def reset(self) -> List[int]:
        self.nums = self.stored[:]
        return self.nums
        

    def shuffle(self) -> List[int]:
        n = len(self.nums)
        for i in range(n):
            j = randint(i, n-1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

"""
hint
use Fisher-Yates algorithm: j = randint(i, n-1) and swapping places elements
i and j
"""
