"""
https://leetcode.com/problems/minimum-time-to-complete-trips/

Category - Medium

You are given an array time where time[i] denotes the time taken by the ith
bus to complete one trip.

Each bus can make multiple trips successively; that is, the next trip can
start immediately after completing the current trip. Also, each bus operates
independently; that is, the trips of one bus do not influence the trips of any
other bus.

You are also given an integer totalTrips, which denotes the number of trips
all buses should make in total. Return the minimum time required for all buses
to complete at least totalTrips trips.
"""

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, max(time) * totalTrips
        while left <= right:
            mid = left + (right - left) // 2
            tmp = sum([mid // t for t in time])
            if tmp >= totalTrips:
                right = mid - 1
            else:
                left = mid + 1
        return left
