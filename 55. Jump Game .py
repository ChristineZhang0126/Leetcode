# 55. Jump Game
# Medium
# 18.5K
# 1.1K
# Companies
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105
# not working
# class Solution(object):
#     def canJump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         # brute force
#         new_hash = {}
#         new_hash[0] = [i for i in range(nums[0] + 1)]
        
#         for each in range(1, len(nums)):
#             new_hash[each] = []
            
#         for each in new_hash:
#             for all_ele in new_hash[each]:
#                 for i in range(nums[each] + 1):
#                     if all_ele + i < len(nums):
#                         new_hash[each + i].append(all_ele)
#                         if each + i == len(nums) - 1:
#                             return True
#         return False
class Solution(object):
    def canJump(self, nums):
        goal = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False