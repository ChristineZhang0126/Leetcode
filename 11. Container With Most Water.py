# 11. Container With Most Water
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1


            
# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         max_area = 0
#         for each in range(len(height)):
#             r = each + 1
#             while r < len(height):
#                 max_area = max(max_area, (r - each) * min(height[each],height[r]))

#                 r+=1
#         return max_area
class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            if height[left] < height[right]:
                max_area = max((right - left ) *  height[left],max_area)
                left += 1
            elif height[left] > height[right]:
                max_area = max((right - left) *  height[right],max_area)
                right -= 1
            else:
                max_area = max((right - left) *  height[right],max_area)
                left += 1
                right -= 1

        return max_area
        
