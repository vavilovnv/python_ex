"""
https://leetcode.com/problems/swap-nodes-in-pairs/

Category - Medium

Given a linked list, swap every two adjacent nodes and return its head. You
must solve the problem without modifying the values in the list's nodes (i.e.,
only nodes themselves may be changed.)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(0)
        prev.next = head
        while prev.next and prev.next.next:
            x, y = prev.next, prev.next.next
            next_pair_node = prev.next.next.next
            prev.next, prev.next.next = y, x
            prev.next.next.next = next_pair_node
            prev = prev.next.next
        return dummy.next

# hint
# work with prev node is the key
