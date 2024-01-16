# 1091. Shortest Path in Binary Matrix
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

 

# Example 1:


# Input: grid = [[0,1],[1,0]]
# Output: 2
# Example 2:


# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
# class Solution(object):
#     def shortestPathBinaryMatrix(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         visited = set()

#         def dfs(col, row, distance):
#             if 0 <= col < len(grid) and 0 <= row < len(grid[0]) and grid[col][row] == 0 and (col, row) not in visited:
#                 visited.add((col, row))

#                 if col == len(grid) - 1 and row == len(grid[0]) - 1:
#                     return distance  # Reached the destination

#                 return min(
#                     dfs(col + 1, row, distance + 1),
#                     dfs(col, row + 1, distance + 1),
#                     dfs(col - 1, row, distance + 1),
#                     dfs(col, row - 1, distance + 1),
                   
#                 )

#             return float('inf')  # Return infinity if the path is not valid

#         result = dfs(0, 0, 1)

#         return result if result != float('inf') else -1
from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        queue = deque([(0, 0, 1)])  # (row, col, distance)

        while queue:
            current_row, current_col, distance = queue.popleft()

            if current_row == rows - 1 and current_col == cols - 1:
                return distance

            for dr, dc in directions:
                new_row, new_col = current_row + dr, current_col + dc

                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 0:
                    queue.append((new_row, new_col, distance + 1))
                    grid[new_row][new_col] = 1  # Mark as visited

        return -1  # No valid path found

