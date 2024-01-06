# 200. Number of Islands
# Medium
# 21.8K
# 473
# Companies
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        def dfs(row, col):
            # Check if the current cell is within the grid boundaries and is part of an island
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == '1':
                # Mark the current cell as visited
                grid[row][col] = '0'
                
                # Explore the adjacent cells in a depth-first manner
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)


        island_count = 0
    
        # Traverse the entire grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If the current cell is part of an unvisited island, perform DFS
                if grid[i][j] == '1':
                    island_count += 1
                    dfs(i, j)

        return island_count
        
        

        