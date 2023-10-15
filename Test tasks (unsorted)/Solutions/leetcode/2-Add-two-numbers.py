"""
https://leetcode.com/problems/add-two-numbers/

Category - Medium

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d1, d2 = [], []
        
        while l1.next:
            d1.append(str(l1.val))
            l1 = l1.next
        d1.append(str(l1.val))
        while l2.next:
            d2.append(str(l2.val))
            l2 = l2.next
        d2.append(str(l2.val))
        
        for i, v in enumerate(str(int(''.join(d1[::-1])) + int(''.join(d2[::-1])))):
            if i == 0: 
                l3 = ListNode(int(v))
            else:
                l3 = ListNode(int(v), l3)
        return l3
