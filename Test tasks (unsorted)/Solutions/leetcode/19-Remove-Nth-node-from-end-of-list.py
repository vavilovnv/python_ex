"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Category - Medium

Given the head of a linked list, remove the nth node from the end of the list
and return its head.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        if slow.next:
            slow.next = slow.next.next
        return head
