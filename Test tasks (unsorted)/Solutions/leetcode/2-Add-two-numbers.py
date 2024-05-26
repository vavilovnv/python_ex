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

# approach with 2 additional lists

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

# approach without 2 additional lists
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp, dummy = 0, ListNode(0)
        curr = dummy
        
        curr1, curr2 = l1, l2
        while curr1 and curr2:
            val = curr1.val + curr2.val + tmp
            tmp = val // 10
            curr.next = ListNode(val % 10)
            curr = curr.next
            curr1 = curr1.next
            curr2 = curr2.next

        curr3 = curr1 or curr2
        while curr3:
            val = curr3.val + tmp
            tmp = val // 10
            curr.next = ListNode(val % 10)
            curr = curr.next
            curr3 = curr3.next
        
        if tmp:
            curr.next = ListNode(tmp)
            
        return dummy.next
