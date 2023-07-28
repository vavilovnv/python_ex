"""
https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

Category - Medium

You are given a floating-point number hour, representing the amount of time
you have to reach the office. To commute to the office, you must take n
trains in sequential order. You are also given an integer array dist of
length n, where dist[i] describes the distance (in kilometers) of the ith
train ride.

Each train can only depart at an integer hour, so you may need to wait in
between each train ride.

For example, if the 1st train ride takes 1.5 hours, you must wait for an
additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour
mark.
Return the minimum positive integer speed (in kilometers per hour) that all
the trains must travel at for you to reach the office on time, or -1 if it is
impossible to be on time.

Tests are generated such that the answer will not exceed 107 and hour will
have at most two digits after the decimal point.
"""

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) == 1:
            return ceil(round(dist[0] / hour, 2))
        if len(dist) - 1 >= hour:
            return -1
        
        hour_for_last = round(hour - len(dist) + 1, 2)
        min_speed = max_speed = ceil(dist[-1] / hour_for_last)
        if round(hour % 1, 2):
            max_speed = ceil(dist[-1] / round(hour % 1, 2))
        result = max_speed = max(max_speed, max(dist))
        if hour_for_last <= 1:
            return max_speed
        
        while min_speed <= max_speed:
            mid_speed, hours_count = (min_speed + max_speed) // 2, 0
            for i in range(len(dist) - 1):
                hours_count += ceil(dist[i] / mid_speed)
            hours_count += dist[-1] / mid_speed
            if 0 <= round(hour - hours_count, 2):
                result = min(result, mid_speed)
            if round(hour - hours_count, 2) > 0:
                max_speed = mid_speed - 1
            else:
                min_speed = mid_speed + 1
        return result
