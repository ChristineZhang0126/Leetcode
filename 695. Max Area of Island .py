# 695. Max Area of Island
# Medium
# 9.7K
# 198
# Companies
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

 

# Example 1:


# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0

        def dfs(each, i, the_area):
            if 0 <= each < len(grid) and 0 <= i < len(grid[0]) and grid[each][i] == 1:
                grid[each][i] = 0
                the_area += 1
                the_area = dfs(each + 1, i, the_area)
                the_area = dfs(each - 1, i, the_area)
                the_area = dfs(each, i + 1, the_area)
                the_area = dfs(each, i - 1, the_area)
            return the_area

        for each in range(len(grid)):
            for i in range(len(grid[0])):
                if grid[each][i] == 1:
                    max_area = max(max_area, dfs(each, i, 0))

        return max_area


        