"""
https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

Category - Medium

You are given a 0-indexed integer array buses of length n, where buses[i]
represents the departure time of the ith bus. You are also given a 0-indexed
integer array passengers of length m, where passengers[j] represents the
arrival time of the jth passenger. All bus departure times are unique. All
passenger arrival times are unique.

You are given an integer capacity, which represents the maximum number of
passengers that can get on each bus.

When a passenger arrives, they will wait in line for the next available bus.
You can get on a bus that departs at x minutes if you arrive at y minutes
where y <= x, and the bus is not full. Passengers with the earliest arrival
times get on the bus first.

More formally when a bus arrives, either:

If capacity or fewer passengers are waiting for a bus, they will all get on
the bus, or
The capacity passengers with the earliest arrival times will get on the bus.
Return the latest time you may arrive at the bus station to catch a bus. You
cannot arrive at the same time as another passenger.

Note: The arrays buses and passengers are not necessarily sorted.
"""

from collections import deque

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        res, last_passenger, passengers = 0, None, deque(passengers)
        for bus in buses:
            aviable_places = capacity
            while passengers and passengers[0] <= bus and aviable_places:
                aviable_places -= 1
                if not last_passenger or last_passenger < passengers[0] - 1:
                    res = passengers[0] - 1
                last_passenger = passengers.popleft()
            if aviable_places and (not last_passenger or last_passenger < bus):
                res = bus
        return res
