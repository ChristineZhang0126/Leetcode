# 110. Balanced Binary Tree
# Solved
# Easy
# Topics
# Companies
# Given a binary tree, determine if it is 
# height-balanced
# .

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # base case
        if not root:
            return True
        def depth(root):
            if not root:
                return 0
            else:
                return max(depth(root.left), depth(root.right)) + 1


        if max(depth(root.left),depth(root.right)) - min(depth(root.left),depth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
