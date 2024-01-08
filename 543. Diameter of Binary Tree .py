# 543. Diameter of Binary Tree
# Easy
# 12.9K
# 846
# Companies
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100
# class Solution(object):
#     def diameterOfBinaryTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root is None:
#             return 0

#         max_diameter = 0

#         # Calculate the depth of the left subtree
#         left_way = 0
#         temp_left = root
#         while temp_left.left:
#             left_way += 1
#             temp_left = temp_left.left

#         # Calculate the depth of the right subtree
#         right_way = 0
#         temp_right = root
#         while temp_right.right:
#             right_way += 1
#             temp_right = temp_right.right

#         # Update the maximum diameter considering the left and right ways
#         max_diameter = max(max_diameter, left_way + right_way)

#         # Recursively call the function for left and right subtrees
#         self.diameterOfBinaryTree(root.left)
#         self.diameterOfBinaryTree(root.right)

#         return max_diameter

# the idea would be: the longest path will alwasy occur in  res[0] = max(res[0],2+right+left)
# the left subtree and right subtree plus 2 for each node
class Solution(object):
    def diameterOfBinaryTree(self, root):
        res = [0]
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0],2+right+left)
            return 1 + max(left,right)
        dfs(root)
        return res[0]


        