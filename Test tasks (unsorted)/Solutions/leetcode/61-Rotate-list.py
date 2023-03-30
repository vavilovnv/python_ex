"""
https://leetcode.com/problems/rotate-list/

Category - Medium

Given the head of a linked list, rotate the list to the right by k places.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        nodes, node = 1, head
        while node.next:
            node = node.next
            nodes += 1
        node.next = head
        k = nodes - (k % nodes)
        while k > 0:
            node = node.next
            k -= 1
        head = node.next
        node.next = None
        return head

"""
hints
Calculate the length of the list and loop it. Take k = nodes - (k % nodes).
Move head by k. Break the list.
"""
