# 15. 3Sum
# Medium
# 29.5K
# 2.7K
# Companies
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # return_list = []
        # for i in nums:
        #     new = i + 1
        #     for each in nums[i+1:len(nums)-1]:
        #         if (0 - i - each) in nums[new + 1:]:
        #             if sorted([i, each, 0-i-each]) not in return_list:
        #                 return_list.append(sorted([i, each, 0-i-each]))
        #         new += 1
        
        # return return_list
        #[-4,-1,-1,0,1,2]
        final_output = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                
                if (nums[i] + nums[l] + nums[r]) < 0:
                    l += 1
                elif (nums[i] + nums[l] + nums[r]) > 0:
                    r -=1
                else:
                    a_list = [nums[i],nums[l], nums[r]]
                    if a_list not in final_output:
                        final_output.append(a_list)
                    l += 1
                    r -=1
        return final_output
