"""
https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

Category - Medium

You are given an array of integers nums and the head of a linked list. Return
the head of the modified linked list after removing all nodes from the linked
list that have a value that exists in nums.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy, s = ListNode(next=head), set(nums)
        node = dummy
        while node.next:
            if node.next.val in s:
                node.next = node.next.next
            else:
                node = node.next
        return dummy.next
