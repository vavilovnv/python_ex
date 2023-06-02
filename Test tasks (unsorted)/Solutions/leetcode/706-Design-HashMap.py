"""
https://leetcode.com/problems/design-hashmap/

Category - Easy

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If
the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1
if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map
contains the mapping for the key.
"""

class MyHashMap:

    def __init__(self):
        self._keys = set()
        self._values = []
        

    def put(self, key: int, value: int) -> None:
        if key not in self._keys:
            self._keys.add(key)
            self._values.append([key, value])
        else:
            element = [i for i in self._values if i[0] == key][0]
            element[1] = value
        
        

    def get(self, key: int) -> int:
        if key in self._keys:
            element = [i for i in self._values if i[0] == key][0]
            return element[1]
        return -1
        

    def remove(self, key: int) -> None:
        if key in self._keys:
            self._keys.remove(key)
            element = [i for i in self._values if i[0] == key][0] 
            self._values.remove(element)  
