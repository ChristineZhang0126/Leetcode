# 938. Range Sum of BST
# Solved
# Easy
# Topics
# Companies
# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

# Example 1:


# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
# Example 2:


# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        the_sum = 0
        queue = [root]
        #visited = []
        while queue:
            len_queue = len(queue)
            for i in range(len_queue):
                the_pop = queue.pop()
                if  low <= the_pop.val <= high:
                    the_sum += the_pop.val
                if the_pop.left:
                    queue.append(the_pop.left)
                if the_pop.right:
                    queue.append(the_pop.right)
        return the_sum
