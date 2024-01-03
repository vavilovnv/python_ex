"""
https://leetcode.com/problems/minimum-number-of-refueling-stops/

Category - Hard

A car travels from a starting position to a destination which is target miles
east of the starting position.

There are gas stations along the way. The gas stations are represented as an
array stations where stations[i] = [positioni, fueli] indicates that the ith
gas station is positioni miles east of the starting position and has fueli
liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel
liters of fuel in it. It uses one liter of gas per one mile that it drives.
When the car reaches a gas station, it may stop and refuel, transferring all
the gas from the station into the car.

Return the minimum number of refueling stops the car must make in order to
reach its destination. If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can
still refuel there. If the car reaches the destination with 0 fuel left, it
is still considered to have arrived.
"""

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])
        res, heap = 0, []
        for pos, fuel in stations:
            while heap and pos > startFuel:
                startFuel -= heapq.heappop(heap)
                res += 1
            if pos > startFuel:
                return -1
            heapq.heappush(heap, -fuel)
        return res
