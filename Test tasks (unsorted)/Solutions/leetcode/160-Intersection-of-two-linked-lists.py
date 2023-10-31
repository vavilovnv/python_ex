"""
https://leetcode.com/problems/intersection-of-two-linked-lists/

Category - Easy

Given the heads of two singly linked-lists headA and headB, return the node at
which the two lists intersect. If the two linked lists have no intersection at
all, return null.

For example, the following two linked lists begin to intersect at node c1:
The test cases are generated such that there are no cycles anywhere in the
entire linked structure.

Note that the linked lists must retain their original structure after the 
unction returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these 
nputs):
intersectVal - The value of the node where the intersection occurs. This is 0
if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to
get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to
get to the intersected node.
The judge will then create the linked structure based on these inputs and pass
the two heads, headA and headB to your program. If you correctly return the
intersected node, then your solution will be accepted.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_a, node_b = headA, headB
        while node_a != node_b:
            node_a = node_a.next if node_a else headB
            node_b = node_b.next if node_b else headA
        return node_a
