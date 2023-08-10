"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Category - Easy

Given the head of a sorted linked list, delete all duplicates such that each
element appears only once. Return the linked list sorted as well.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        root = head
        while root.next:
            if root.val == root.next.val:
                root.next = root.next.next
            else:
                root = root.next
        return head    
