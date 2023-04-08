"""
https://leetcode.com/problems/bulls-and-cows/

Category - Medium

You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number
is. When your friend makes a guess, you provide a hint with the following
info:
The number of "bulls", which are digits in the guess that are in the correct
position.
The number of "cows", which are digits in the guess that are in your secret
number but are located in the wrong position. Specifically, the non-bull
digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint
for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y
is the number of cows. Note that both secret and guess may contain duplicate
 digits.
"""

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        secret_d, guess_d = defaultdict(int), defaultdict(int)
        for i, v in enumerate(secret):
            if v == guess[i]:
                bulls += 1
            else:
                if v in guess_d and guess_d[v] > 0:
                    guess_d[v] -= 1
                    cows += 1
                else:
                    secret_d[v] += 1
                if guess[i] in secret_d and secret_d[guess[i]] > 0:
                    secret_d[guess[i]] -= 1
                    cows += 1
                else:
                    guess_d[guess[i]] += 1
        return f'{bulls}A{cows}B'
