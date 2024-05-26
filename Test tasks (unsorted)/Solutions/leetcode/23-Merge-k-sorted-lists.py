"""
https://leetcode.com/problems/merge-k-sorted-lists/

Category - Hard

You are given an array of k linked-lists lists, each linked-list is sorted in
ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for root in lists:
            if root:
                heapq.heappush(heap, (root.val, id(root), root))

        dummy = ListNode()
        current = dummy
        while heap:
            *_, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, id(node.next), node.next))

        return dummy.next
