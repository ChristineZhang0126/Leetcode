# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Medium
# 14.3K
# 449
# Companies
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
 

# Constraints:

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.

#Solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # the first node of preorder is always the root and 
        # anything on the left of root in inorder are the left subtree 
        # anything ont he right of the root in inorder are the right subtree
        # partition left and right in preorder and recursively call buildtree in those partition
        if not preorder :
            return None
        the_root = TreeNode(preorder[0])
        left_in = []
        left_pre = []
        index = 0
        while inorder[index] != preorder[0]:
            index += 1
        right_in = inorder[index+1:]
        left_in = inorder[0:index+1]
        start = 1
        while index > 0:
            left_pre.append(preorder[start])
            start+=1
            index-=1
        right_pre = preorder[start:]
        the_root.left = self.buildTree(left_pre,left_in)
        the_root.right = self.buildTree(right_pre,right_in)
        return the_root
        