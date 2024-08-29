"""
https://leetcode.com/problems/flatten-nested-list-iterator/

Category - Medium

You are given a nested list of integers nestedList. Each element is either an
integer or a list whose elements may also be integers or other lists.
Implement an iterator to flatten it.

Implement the NestedIterator class:
- NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with
the nested list nestedList.
- int next() Returns the next integer in the nested list.
- boolean hasNext() Returns true if there are still some integers in the
nested list and false otherwise.
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self._items = self._to_flatten(nestedList)
    
    def next(self) -> int:
        return self._items.pop()
    
    def hasNext(self) -> bool:
        return len(self._items) > 0

    @staticmethod
    def _to_flatten(nested_list):
        res = []
        for i, item in enumerate(nested_list):
            while not item.isInteger():
                if value := item.getList():
                    nested_list[i:i+1] = value
                    item = nested_list[i]
                else:
                    break
            if item.isInteger():
                res.append(item)
        return res[::-1]

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
