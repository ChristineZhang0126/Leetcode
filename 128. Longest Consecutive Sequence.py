# 128. Longest Consecutive Sequence
# Solved
# Medium
# Topics
# Companies
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
class Solution(object):
    def longestConsecutive(self,nums):
        if not nums:
            return 0

        num_set = set(nums)
        max_length = 0

        for num in num_set:
            # Check if num is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                # Check for consecutive elements
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                # Update the maximum length
                max_length = max(max_length, current_length)

        return max_length

   
 


            

        
