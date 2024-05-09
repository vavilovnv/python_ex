"""
https://leetcode.com/problems/remove-nodes-from-linked-list/

Category - Medium

You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right
side of it.

Return the head of the modified linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = self.reverse_list(head)
        
        head = curr
        while curr and curr.next:
            if curr.val > curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return self.reverse_list(head)
