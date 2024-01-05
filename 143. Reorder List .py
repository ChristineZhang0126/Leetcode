# 143. Reorder List
# Medium
# 10K
# 345
# Companies
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution(object):
#     def reorderList(self, head):
#         """
#         :type head: ListNode
#         :rtype: None Do not return anything, modify head in-place instead.
#         """
#         # two pointers
#         nodes = []
#         current = ListNode()
#         new = current
#         while head:
#             nodes.append(head.val)
#             head = head.next
#         l = 0
#         r = len(nodes)-1
#         n = 1
#        # l = nodes[0]
#         #r = nodes[len(nodes)-1]
#         while l <= r:
#             new_node = ListNode()
#             next_node = ListNode()
#             if l == r:
#                 new_node.val = nodes[l]
#                 current.next = new_node
#             else: 
#                 new_node.val = nodes[l]
#                 next_node.val = nodes[r]
#                 new_node.next = next_node
#                 #print(new_node)
#                 current.next = new_node
#             #print(current.next.next)
#            # n += 1
#             l += 1
#             r -=1
#             current = current.next
#            # print(current)
#         new.next = None
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next

        l, r = 0, len(nodes) - 1

        while l < r:
            nodes[l].next = nodes[r]
            l += 1

            if l == r:
                break

            nodes[r].next = nodes[l]
            r -= 1

        nodes[l].next = None




        
        