# 416. Partition Equal Subset Sum
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
 

# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 != 0:
            return False
        sums = set()
        sums.add(0)
        for i in range(len(nums)-1,-1,-1):
            new = set()
            for t in sums:
                new.add(t)
                new.add(t+nums[i])
            sums = new
        if sum(nums) / 2 not in sums:
            return False
        return True


