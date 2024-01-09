# 215. Kth Largest Element in an Array
# Medium
# 16.5K
# 820
# Companies
# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 

# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # brute force, time complxity is O(nlogn)
        # nums = sorted(nums)
        # return nums[len(nums) - k]
        # heap , O(nlogk) better if k < n
        new_list = []
        for each in nums:
            new_list.append(-each)


        heapq.heapify(new_list)
        #print(nums)
       #print(heapq.heappop(nums))
        while k>0:
            if k == 1:
                return -heapq.heappop(new_list)
            heapq.heappop(new_list)
            k-=1
        
