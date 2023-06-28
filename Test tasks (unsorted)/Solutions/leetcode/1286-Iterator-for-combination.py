"""
https://leetcode.com/problems/iterator-for-combination/

Category - Medium

Design the CombinationIterator class:
* CombinationIterator(string characters, int combinationLength) Initializes
the object with a string characters of sorted distinct lowercase English
letters and a number combinationLength as arguments.
* next() Returns the next combination of length combinationLength in
lexicographical order.
* hasNext() Returns true if and only if there exists a next combination.
"""

from itertools import combinations

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self._iter = self._comb(characters, combinationLength)
        self._next = None

    def next(self) -> str:
        if self._next is not None:
            result = self._next
            self._next = None
            return result
        return next(self._iter)

    def hasNext(self) -> bool:
        if self._next is not None:
            return True
        try:
            self._next = next(self._iter)
        except StopIteration:
            return False
        return True
        
    @staticmethod
    def _comb(characters: str, combinationLength: int):
        for comb in combinations(characters, combinationLength):
            yield ''.join(list(comb))

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
            