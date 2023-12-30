# 1. Two Sum
# Easy
# 54.1K
# 1.8K
# Companies
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 
# hash map
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_indices = {}  # Hash map to store indices of elements

        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement is in the hash map
            if complement in num_indices:
                # Return the indices of the two numbers that add up to the target
                return [num_indices[complement], i]

            # Add the current number and its index to the hash map
            num_indices[num] = i

        # If no solution is found
        return None
    
# two pointer
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # two pointer:
        new_nums = sorted(nums)
        l = 0
        r = len(new_nums)-1
        while l < r:
            if new_nums[l] + new_nums[r] > target:
                r-=1
            elif new_nums[l] + new_nums[r] < target:
                l += 1
            elif new_nums[l] + new_nums[r] == target:
                the_list = []
                the_list.append(nums.index(new_nums[l]))
                nums[nums.index(new_nums[l])] = ''
                the_list.append(nums.index(new_nums[r]))
                return the_list
        
        