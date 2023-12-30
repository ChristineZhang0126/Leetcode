# 217. Contains Duplicate
# Easy
# 11.3K
# 1.3K
# Companies
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        new = set()
        for each in nums:
            if each not in new:
                new.add(each)
            else:
                return True
        return False

