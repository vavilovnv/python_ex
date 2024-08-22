"""
https://leetcode.com/problems/time-based-key-value-store/

Category - Medium

Design a time-based key-value data structure that can store multiple values
for the same key at different time stamps and retrieve the key's value at a
certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the
value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called
previously, with timestamp_prev <= timestamp. If there are multiple such
values, it returns the value associated with the largest timestamp_prev. If
there are no values, it returns "".
"""

class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        res, lst = "", self.d.get(key)
        if not lst:
            return res
        
        left, right = 0, len(lst) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if lst[mid][1] <= timestamp:
                res = lst[left][0]
                left = mid + 1
            else:
                right = mid - 1
        return res
