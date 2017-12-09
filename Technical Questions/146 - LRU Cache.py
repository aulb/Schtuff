from collections import OrderedDict
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.max_size = capacity
        self.used_slots = 0
        self.storage = OrderedDict()
        
    def is_full(self):
        """
        :rtype: bool
        """
        return self.used_slots == self.max_size

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # If it exist, need to update to put in "front"
        if key in self.storage:
            value = self.storage.pop(key)
            self.storage[key] = value
            return value
        else: return -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # If key is in storage, need to "refresh"
        if key in self.storage:
            self.storage.pop(key)
        # If key not there, check if its full, if it is then pop the end of the array
        else:
            if self.is_full(): self.storage.popitem(False)
            else: self.used_slots += 1
        self.storage[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
