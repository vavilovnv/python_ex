"""
https://leetcode.com/problems/reveal-cards-in-increasing-order/

Category - Medium

You are given an integer array deck. There is a deck of cards where every card
has a unique integer. The integer on the ith card is deck[i].

You can order the deck in any order you want. Initially, all the cards start
face down (unrevealed) in one deck.

You will do the following steps repeatedly until all cards are revealed:

Take the top card of the deck, reveal it, and take it out of the deck.
If there are still cards in the deck then put the next top card of the deck at
the bottom of the deck.
If there are still unrevealed cards, go back to step 1. Otherwise, stop.
Return an ordering of the deck that would reveal the cards in increasing
order.

Note that the first entry in the answer is considered to be the top of the
deck.
"""

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        q = collections.deque(range(len(deck)))
        res = [None] * len(deck)

        for card in deck:
            i = q.popleft()
            res[i] = card
            if q:
                q.append(q.popleft())
        return res
        