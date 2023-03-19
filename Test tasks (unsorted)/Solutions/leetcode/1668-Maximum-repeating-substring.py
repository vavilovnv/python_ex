"""
https://leetcode.com/problems/maximum-repeating-substring/

Category - Easy

For a string sequence, a string word is k-repeating if word concatenated k
times is a substring of sequence. The word's maximum k-repeating value is the
highest value k where word is k-repeating in sequence. If word is not a
substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word
in sequence.
"""

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if word not in sequence:
            return 0
        # Count the number of occurrences of word-length strings in the sequence
        count = len(sequence) // len(word)
        # In the loop, we check if the `word*(count-i) string` is in the sequence
        for i in range(count):
            if word * (count - i) in sequence:
                return count - i
