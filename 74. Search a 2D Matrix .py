# 74. Search a 2D Matrix
# Medium
# 15.1K
# 399
# Companies
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # binary search
        len_row = len(matrix[0])
        for each in range(len(matrix)):
            l = 0
            r = len_row - 1
            #mid = l + (r-l) // 2
            while l <= r:
                mid = l + (r-l) // 2
                if target == matrix[each][mid]:
                    return True
                elif target > matrix[each][mid]:
                    l = mid + 1
                elif target < matrix[each][mid]:
                    r = mid - 1
        return False
        

        