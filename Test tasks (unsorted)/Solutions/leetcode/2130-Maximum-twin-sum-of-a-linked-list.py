"""
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

Category - Medium

In a linked list of size n, where n is even, the ith node (0-indexed) of the
linked list is known as the twin of the (n-1-i)th node, if 
0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the
twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum
of the linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# TC: O(n) SC: O(n/2)
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res, arr = 0, []
        slow = fast = head
        while fast:
            arr.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        while slow:
            v = arr.pop()
            if v + slow.val > res:
                res = v + slow.val
            slow = slow.next
        return res
