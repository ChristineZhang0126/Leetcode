# 102. Binary Tree Level Order Traversal
# Solved
# Medium
# Topics
# Companies
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #BFS
        if root is None:
            return None
        queue = [root]
        return_list = []
        while queue:
            len_return = len(queue)
            another_list = []
            for each in range(len_return):
                the_pop = queue.pop(0)
                if the_pop.left:
                    queue.append(the_pop.left)
                if the_pop.right:
                    queue.append(the_pop.right)
                another_list.append(the_pop.val)
            return_list.append(another_list)
        return return_list

