"""
https://leetcode.com/problems/palindrome-linked-list/

Category - Easy

Given the head of a singly linked list, return true if it is a palindrome or
false otherwise.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# TC: O(n) SC: O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst == lst[::-1]
    
# TC: O(n) SC: O(1)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next and fast.next:
            slow = slow.next
            fast = fast.next.next
        node, prev = slow, None
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
