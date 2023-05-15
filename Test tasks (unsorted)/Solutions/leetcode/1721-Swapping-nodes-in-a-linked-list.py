"""
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

Category - Medium

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node
from the beginning and the kth node from the end (the list is 1-indexed).
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = right = head
        for i in range(k-1):
            left = left.next
        right_fast = left
        while right_fast.next:
            right = right.next
            right_fast = right_fast.next
        left.val, right.val = right.val, left.val
        return head  
