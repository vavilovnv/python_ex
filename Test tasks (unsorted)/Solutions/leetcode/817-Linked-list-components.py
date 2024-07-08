"""
https://leetcode.com/problems/linked-list-components/

Category - Medium

You are given the head of a linked list containing unique integer values and
an integer array nums that is a subset of the linked list values.

Return the number of connected components in nums where two values are
connected if they appear consecutively in the linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        res, conn, n = 0, False, set(nums)
        curr = head
        while curr:
            if curr.val in n:
                if not conn:
                    res += 1
                    conn = True
            else:
                conn = False
            curr = curr.next
        return res
