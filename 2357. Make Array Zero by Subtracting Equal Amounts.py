# 2357. Make Array Zero by Subtracting Equal Amounts
# Solved
# Easy
# Topics
# Companies
# Hint
# You are given a non-negative integer array nums. In one operation, you must:

# Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
# Subtract x from every positive element in nums.
# Return the minimum number of operations to make every element in nums equal to 0.

 

# Example 1:

# Input: nums = [1,5,0,3,5]
# Output: 3
# Explanation:
# In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
# In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
# In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].
# Example 2:

# Input: nums = [0]
# Output: 0
# Explanation: Each element in nums is already 0 so no operations are needed.
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_return = 0
        while nums != [0] * len(nums):
            new = 0
            while new < len(nums):
                if nums[new] == 0:
                    new += 1
                else:
                    min_num = nums[new]
                    break
            
            for each in range(new, len(nums)):
                if nums[each] != 0:
                    if nums[each] < min_num and nums[each] != 0:
                        min_num = nums[each]
            for i in range(len(nums)):
                if nums[i] > 0:
                    nums[i] = nums[i] - min_num
                    #nums[i] = 0
            min_return += 1
            #nums = 
        return min_return
    
    #return len(set(nums)) - (0 in set(nums))