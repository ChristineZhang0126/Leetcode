# 238. Product of Array Except Self
# Medium
# 21K
# 1.2K
# Companies
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_0 = 0
        total_pro = 1
        index_0 = 0
        for i in nums:
            if i == 0:
                num_0 += 1
                index_0 = nums.index(i)
            else:
                total_pro *= i
            
        if num_0 >= 2:
            return [0] * len(nums)
        else:
            if num_0 == 1:
                a_list = [0] * len(nums)
                a_list[index_0] = total_pro
                return a_list
            elif num_0 == 0:
                the_list = []
                for each in nums:
                    the_list.append(total_pro /each)
                return the_list
                    
