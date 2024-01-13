# Description
# There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

# The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

# Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

# Example 1:

# Input: heights = [4,2,3,1]

# Output: [0,2,3]

# Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.

# Example 2:

# Input: heights = [4,3,2,1]

# Output: [0,1,2,3]

# Explanation: All the buildings have an ocean view.

# Example 3:

# Input: heights = [1,3,2,4]

# Output: [3]

# Explanation: Only building 3 has an ocean view.

# Example 4:

# Input: heights = [2,2,2,2]

# Output: [3]

# Explanation: Buildings cannot see the ocean if there are buildings of the same height to its right.

# Constraints:

# 1 <= heights.length <= 10^5
# 1 <= heights[i] <= 10^9
class Solution:
    def findBuildings(self, heights):
        mx = 0
        ocean_view_buildings = []
        
        # Loop over heights backwards
        for i in range(len(heights) - 1, -1, -1):
            current_height = heights[i]
            
            # Check if the building has an ocean view
            if mx < current_height:
                ocean_view_buildings.append(i)
                mx = current_height
        
        # Return the indices of buildings that have an ocean view in increasing order
        return ocean_view_buildings[::-1]



