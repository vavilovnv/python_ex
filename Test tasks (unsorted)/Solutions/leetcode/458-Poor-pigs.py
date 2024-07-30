"""
https://leetcode.com/problems/poor-pigs/

Category - Hard

There are buckets buckets of liquid, where exactly one of the buckets is
poisonous. To figure out which one is poisonous, you feed some number of
(poor) pigs the liquid to see whether they will die or not. Unfortunately, you
only have minutesToTest minutes to determine which bucket is poisonous.

You can feed the pigs according to these steps:

Choose some live pigs to feed.
For each pig, choose which buckets to feed it. The pig will consume all the
chosen buckets simultaneously and will take no time. Each pig can feed from
any number of buckets, and each bucket can be fed from by any number of pigs.
Wait for minutesToDie minutes. You may not feed any other pigs during this
time.
After minutesToDie minutes have passed, any pigs that have been fed the
poisonous bucket will die, and all others will survive.
Repeat this process until you run out of time.
Given buckets, minutesToDie, and minutesToTest, return the minimum number of
pigs needed to figure out which bucket is poisonous within the allotted time.
"""

# TC O(logN), where N there is buckets
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        res, steps = 0, minutesToTest // minutesToDie + 1
        while steps ** res < buckets:
            res += 1
        return res
        