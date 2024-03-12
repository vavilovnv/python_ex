"""
https://leetcode.com/problems/seat-reservation-manager/

Category - Medium

Design a system that manages the reservation state of n seats that are
numbered from 1 to n.

Implement the SeatManager class:

SeatManager(int n) Initializes a SeatManager object that will manage n seats
numbered from 1 to n. All seats are initially available.
int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and
returns its number.
void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.
"""

# approach 1
class SeatManager:

    def __init__(self, n: int):
        self._seats = [i + 1 for i in range(n)]
        

    def reserve(self) -> int:
        return heapq.heappop(self._seats)
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self._seats, seatNumber)


# approach 2
class SeatManager:

    def __init__(self, n: int):
        self._seats = []
        self._min_seat = 1

    def reserve(self) -> int:
        if self._seats:
            return heapq.heappop(self._seats)

        num = self._min_seat
        self._min_seat += 1
        return num
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self._seats, seatNumber)       


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
