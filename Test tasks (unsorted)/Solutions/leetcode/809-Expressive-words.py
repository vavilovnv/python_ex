"""
https://leetcode.com/problems/expressive-words/

Category - Easy

Sometimes people repeat letters to represent extra feeling. For example:

"hello" -> "heeellooo"
"hi" -> "hiiii"
In these strings like "heeellooo", we have groups of adjacent letters that are
all the same: "h", "eee", "ll", "ooo".

You are given a string s and an array of query strings words. A query word is
stretchy if it can be made to be equal to s by any number of applications of
the following extension operation: choose a group consisting of characters c,
and add some number of characters c to the group so that the size of the group
is three or more.

For example, starting with "hello", we could do an extension on the group "o"
to get "hellooo", but we cannot get "helloo" since the group "oo" has a size
less than three. Also, we could do another extension like "ll" -> "lllll" to
get "helllllooo". If s = "helllllooo", then the query word "hello" would be
stretchy because of these two extension operations: query = "hello" ->
"hellooo" -> "helllllooo" = s.

Return the number of query strings that are stretchy.
"""

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def helper(word):
            curr, count, letters = word[0], 1, []
            for c in word[1:]:
                if c != curr:
                    letters.append([curr, count])
                    curr, count = c, 1
                else:
                    count += 1
            letters.append([curr, count])
            return letters
        
        res, s_letters = 0, helper(s)
        len_s_letters = len(s_letters)
        for word in words:
            word_letters = helper(word)
            if len_s_letters == len(word_letters):
                for i, v in enumerate(s_letters):
                    letter1, count1 = v
                    letter2, count2 = word_letters[i]
                    if (letter1 != letter2
                        or (count2 != count1 and (count2 > count1 or count1 < 3))):
                        break
                else:
                    res += 1
        return res
