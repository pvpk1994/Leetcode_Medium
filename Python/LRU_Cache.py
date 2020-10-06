# Least Recently Used Cache using Ordered Dictionary (HashMap + Linkedlist)
# Author: Pavan Kumar Paluri
# Using Constant linear time complexity 

from collections import OrderedDict
# A simple hash-map can handle get() 
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        # since this key is being referenced, it should be moved to the last
        self.move_to_end(key, last=True)
        return self[key]
        
    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key, last=True)
        # add kay-value to cache
        self[key]=value
        # evict least recently used in case buffer is full
        if len(self) > self.capacity:
            self.popitem(last=False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
