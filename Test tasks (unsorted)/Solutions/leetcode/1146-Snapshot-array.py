"""
https://leetcode.com/problems/snapshot-array/

Category - Medium

Implement a SnapshotArray that supports the following interface:
* SnapshotArray(int length) initializes an array-like data structure with the
given length. Initially, each element equals 0.

* void set(index, val) sets the element at the given index to be equal to val.

* int snap() takes a snapshot of the array and returns the snap_id: the total
number of times we called snap() minus 1.

* int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
"""

class SnapshotArray:

    def __init__(self, length: int):
        self._data = defaultdict(list)
        self._snapshots = 0
        

    def set(self, index: int, val: int) -> None:
        self._data[index].append([self._snapshots, val])
        

    def snap(self) -> int:
        self._snapshots += 1
        return self._snapshots - 1
        

    def get(self, index: int, snap_id: int) -> int:
        arr = self._data[index]
        res, left, right = -1, 0, len(arr)-1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid][0] <= snap_id:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        if res == -1:
            return 0
        return arr[res][1]
