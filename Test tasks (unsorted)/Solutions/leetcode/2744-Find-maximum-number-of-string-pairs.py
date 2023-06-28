"""
https://leetcode.com/problems/find-maximum-number-of-string-pairs/

Category - Easy

You are given a 0-indexed array words consisting of distinct strings.

The string words[i] can be paired with the string words[j] if:

The string words[i] is equal to the reversed string of words[j].
0 <= i < j < words.length.
Return the maximum number of pairs that can be formed from the array words.

Note that each string can belong in at most one pair.
"""

# TC: O(n) SC: O(n)
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        d = defaultdict(int)
        for i in words:
            d[max(i, i[::-1])] += 1
        return len([k for k, v in d.items() if v > 1])
