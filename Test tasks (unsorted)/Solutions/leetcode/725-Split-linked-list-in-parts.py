"""
https://leetcode.com/problems/split-linked-list-in-parts/

Category - Medium

Given the head of a singly linked list and an integer k, split the linked
list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should
have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts
occurring earlier should always have a size greater than or equal to parts
occurring later.

Return an array of the k parts.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        root = head
        if not root:
            return [None for i in range(k)]
        res, len_list = [], 0
        
        while root:
            len_list += 1
            root = root.next
        root = head

        count, change = divmod(len_list, k)
        for _ in range(k):
            new_root = ListNode()
            new_head = new_root
            for _ in range(count + (change > 0)):
                new_root.next, root, new_root = root, root.next, root
            new_root.next = None
            res.append(new_head.next)
            change -= 1
        return res
