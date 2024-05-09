"""
https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

Category - Medium

You are given the head of a non-empty linked list representing a non-negative
integer without leading zeroes.

Return the head of the linked list after doubling it.
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

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = self.reverse_list(head)
        
        mem = 0
        while curr:
            val = curr.val * 2 
            curr.val = mem + (val % 10)
            mem = val // 10
            prev = curr
            curr = curr.next

        if mem:
            prev.next = ListNode(mem)
       
        return self.reverse_list(head)
