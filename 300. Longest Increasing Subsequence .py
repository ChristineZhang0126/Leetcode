# 300. Longest Increasing Subsequence
# Medium
# 19.3K
# 366
# Companies
# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence
# .

 

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # we get the len longest subsequence of each index, and return the the len for nums[len-1]
        len_array = []
        for each in range(len(nums)):
            len_array.append(0)
        for each in range(len(nums)):
            max_pre_len = 0
            for i in range(len(nums[0:each])):
                if nums[i] < nums[each]:
                    if len_array[i] > max_pre_len:
                        max_pre_len = len_array[i]
            len_array[each] = max_pre_len + 1
        
        return max(len_array)
        