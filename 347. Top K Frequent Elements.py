# 347. Top K Frequent Elements
# Medium
# 16.5K
# 610
# Companies
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        new_map = {}
        return_list = []
        list_for_frequency = []
        for i in nums:
            if i not in new_map:
                new_map[i] = 1
            else:
                new_map[i] += 1

        for freq in new_map.values():
            list_for_frequency.append(-freq)
        heapq.heapify(list_for_frequency)

        # Pop k elements from the heap and append to the result list
        
        while k > 0:
            freq = -heapq.heappop(list_for_frequency)
            for item, a_freq in new_map.items():
                #print(item,a_freq)
                #print("")
                if k > 0:
                    #freq = -heapq.heappop(list_for_frequency)
                   # print(freq)
                    if a_freq == freq:
                        return_list.append(item)
                        k-=1
                        new_map.pop(item)
                        #freq = -heapq.heappop(list_for_frequency)
            
        return return_list