"""
https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

Category - Medium

Given the head of a linked list head, in which each node contains an integer
value.

Between every pair of adjacent nodes, insert a new node with a value equal to
the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer
that evenly divides both numbers.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        @lru_cache
        def get_gcd(a, b):
            return a if b == 0 else get_gcd(b, a % b)
        if not head or not head.next:
            return head
        root = head
        while root.next:
            nxt = root.next
            new_node = ListNode(get_gcd(root.val, root.next.val))
            new_node.next = root.next
            root.next = new_node
            root = nxt
        return head
