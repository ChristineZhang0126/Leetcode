# Dynamic Layout
# Premium
# 0

# avatar
# 146. LRU Cache
# Medium
# 19.9K
# 923
# Companies
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
 

# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.the_list = {}
        self.access_queue = []
        self.capacity = capacity

        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        

        if key not in self.the_list:
            return -1
        else:
            if key in self.access_queue:
                self.access_queue.remove(key)
            self.access_queue.append(key)
            return self.the_list[key]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
       
        if key in self.the_list:
            self.the_list[key] = value
            self.access_queue.remove(key)
            self.access_queue.append(key)
            #self.num[key] += 1
        else:
            if self.capacity > 0:
                self.the_list[key] = value
                self.access_queue.append(key)
                #self.num[key] = 1
                self.capacity -= 1
            elif self.capacity == 0:
                
                self.the_list.pop(self.access_queue[0])
                self.access_queue.remove(self.access_queue[0])
                self.the_list[key] = value
                self.access_queue.append(key)

        