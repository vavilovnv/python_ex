"""
https://leetcode.com/problems/flipping-an-image/

Category - Easy

You are given a string sentence that consist of words separated by spaces.
Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language
similar to Pig Latin.) The rules of Goat Latin are as follows:

If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to
the end of the word.
For example, the word "apple" becomes "applema".
If a word begins with a consonant (i.e., not a vowel), remove the first
letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
Add one letter 'a' to the end of each word per its word index in the
sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets
"aa" added to the end, and so on.
Return the final sentence representing the conversion from sentence to Goat
Latin.
"""

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        res, count = [], 0
        for s in sentence.split():
            count += 1
            word, postfix = "", "a" * count
            if s[0] in "aeiouAEIOU":
                word = s + "ma" + postfix
            else:
                word = s[1:] + s[0] + "ma" + postfix
            res.append(word)
        return " ".join(res)
