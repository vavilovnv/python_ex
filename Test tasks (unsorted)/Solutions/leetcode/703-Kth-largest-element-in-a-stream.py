"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Category - Easy

Design a class to find the kth largest element in a stream. Note that it is
the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and
the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element
representing the kth largest element in the stream.
"""

# list solution 
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k = k
        self._nums = sorted(nums)
        

    def add(self, val: int) -> int:
        self._nums.append(val)
        self._nums.sort()
        return self._nums[-self._k]

# heapq solution
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k = k
        nums = heapq.nlargest(k, nums)
        heapq.heapify(nums)
        self._nums = nums
        

    def add(self, val: int) -> int:
        if len(self._nums) < self._k:
            heapq.heappush(self._nums, val)
        elif val > self._nums[0]:
            heapq.heapreplace(self._nums, val)
        return self._nums[0]
