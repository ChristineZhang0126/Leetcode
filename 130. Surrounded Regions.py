# 130. Surrounded Regions
# Solved
# Medium
# Topics
# Companies
# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

# Example 1:


# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.
# Example 2:

# Input: board = [["X"]]
# Output: [["X"]]
 


# class Solution(object):
#     def solve(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: None Do not return anything, modify board in-place instead.
#         """
#         o_passed = []
#         one_in_bound = False

#         def dfs(each,i):
            
#             if 0 <= each < len(board) and 0 <= i < len(board[0]) and board[each][i] == "X":
#                 if each == 0 or each == len(board) - 1 or i == 0 or i == len(board[0])-1:
#                     one_in_bound = True
#                 dfs(each+1,i)
#                 dfs(each,i+1)
#                 dfs(each-1,i)
#                 dfs(each,i-1)
#             elif 0 <= each < len(board) and 0 <= i < len(board[0]) and board[each][i] == "O":

#                 o_passed.append([each,i])
            
                
        
#         for each in range(1,len(board)-1):
#             for i in range(1,len(board[0])-1):
#                 if board[each][i] == "O":
#                     #print(o_passed)
#                     dfs(each,i)
#                     if not one_in_bound:
#                         for all_i in range(len(o_passed)):
#                             if o_passed[all_i][0] != 0 and o_passed[all_i][0] != len(board)-1 and o_passed[all_i][1] != 0 and o_passed[all_i][1] != len(board[0]) - 1:
#                                 board[o_passed[all_i][0]][o_passed[all_i][1]] = "X"
#                     o_passed = []
#         return board
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def dfs(each, i):
            if 0 <= each < m and 0 <= i < n and board[each][i] == 'O':
                board[each][i] = 'T'  # Mark as temporarily visited
                dfs(each + 1, i)
                dfs(each, i + 1)
                dfs(each - 1, i)
                dfs(each, i - 1)

        # Traverse the border and mark connected 'O's as temporarily visited
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n - 1] == 'O':
                dfs(i, n - 1)

        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m - 1][j] == 'O':
                dfs(m - 1, j)

        # Flip surrounded 'O's to 'X', and revert temporarily visited 'T' back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'

