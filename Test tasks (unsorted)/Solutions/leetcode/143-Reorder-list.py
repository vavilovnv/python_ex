"""
https://leetcode.com/problems/reorder-list/

Category - Medium

You are given the head of a singly linked-list. The list can be represented
as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may
be changed.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        curr, prev = slow.next, None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        slow.next = None

        curr1, curr2 = head, prev
        while curr2:
            tmp1, tmp2 = curr1.next, curr2.next
            curr1.next, curr2.next = curr2, tmp1
            curr1, curr2 = tmp1, tmp2

        return head
