"""
https://leetcode.com/problems/decoded-string-at-index/

Category - Medium

You are given an encoded string s. To decode the string to a tape, the encoded
string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit d, the entire current tape is repeatedly
written d - 1 more times in total.
Given an integer k, return the kth letter (1-indexed) in the decoded string.
"""

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        lengths = [1]
        for letter in s[1:]:
            if lengths[-1] >= k:
                break
            if letter.isdigit():
                lengths.append(lengths[-1] * int(letter))
            else:
                lengths.append(lengths[-1] + 1)
        for i in reversed(range(len(lengths))):
            k %= lengths[i]
            if not k and s[i].isalpha():
                return s[i]
