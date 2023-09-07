"""
https://leetcode.com/problems/reverse-linked-list-ii/

Category - Medium

Given the head of a singly linked list and two integers left and right where
left <= right, reverse the nodes of the list from position left to position
right, and return the reversed list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        d = ListNode(-1)
        d.next = head
        current = head
        count, left_p, right_n = 1, d, head
        while current:
            if count == right:
                right_n = current.next
                current.next = None
                break
            if count < left:
                left_p = left_p.next
            current = current.next
            count += 1
        p = left_p
        current = p.next
        n = current.next
        while n:
            current.next = n.next
            n.next = p.next
            p.next = n
            n = current.next
        current.next = right_n
        return d.next
