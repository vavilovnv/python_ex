"""
https://leetcode.com/problems/sliding-window-maximum/

Category - Hard

You are given an array of integers nums, there is a sliding window of size k
which is moving from the very left of the array to the very right. You can
only see the k numbers in the window. Each time the sliding window moves right
by one position.

Return the max sliding window.
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq, res, left = deque(), [], 0
        for right in range(len(nums)):
            while dq and nums[right] > dq[-1]:
                dq.pop()
            dq.append(nums[right])
            if right - left + 1 == k:
                res.append(dq[0])
                if dq[0] == nums[left]:
                    dq.popleft()
                left += 1
        return res

"""
hint
use deque and keep it monotonically decreasing
"""
