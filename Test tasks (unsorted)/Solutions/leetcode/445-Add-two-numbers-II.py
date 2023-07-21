"""
https://leetcode.com/problems/add-two-numbers-ii/

Category - Medium

You are given two non-empty linked lists representing two non-negative
integers. The most significant digit comes first and each of their nodes
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
        l1_list, l2_list = [], []
        while l1 is not None:
            l1_list.append(l1)
            prev_l1 = l1
            l1, prev_l1.next = l1.next, None
        while l2 is not None:
            l2_list.append(l2)
            prev_l2 = l2
            l2, prev_l2.next = l2.next, None

        head, temp = None, 0
        while l1_list and l2_list:
            l1 = l1_list.pop()
            l2 = l2_list.pop()
            l1.next = head
            head = l1
            head.val = l1.val + l2.val + temp
            temp = 0
            if head.val >= 10:
                temp = 1
                head.val -= 10
        
        while l1_list:
            l1 = l1_list.pop()
            l1.next = head
            head = l1
            head.val += temp
            temp = 0
            if head.val >= 10:
                temp = 1
                head.val -= 10
        while l2_list:
            l2 = l2_list.pop()
            l2.next = head
            head = l2
            head.val += temp
            temp = 0
            if head.val >= 10:
                temp = 1
                head.val -= 10
        if temp:
            node = ListNode(1, head)
            head = node
        return head
        