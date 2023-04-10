"""
https://leetcode.com/problems/top-k-frequent-words/

Category - Medium

Given an array of strings words and an integer k, return the k most frequent
strings.

Return the answer sorted by the frequency from highest to lowest. Sort the
words with the same frequency by their lexicographical order.
"""

# TC: O(n(log(n)))-? MC: O(n)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for word in words:
            d[word] = d.get(word, 0) - 1
        return [i[0] for i in sorted(d.items(), key=lambda x: (x[1], x[0]))[:k]]

# TC: O(n(log(n))) MC: O(n)
def topKFrequent(words, k):
    h = [(-v, k) for k, v in Counter(words).items()]
    heapify(h)
    return [i[1] for i in h[:k]]

"""
hint
use dict and sort or heapq
"""
