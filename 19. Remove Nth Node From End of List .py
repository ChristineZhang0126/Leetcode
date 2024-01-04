# 19. Remove Nth Node From End of List
# Medium
# 17.7K
# 740
# Companies
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        new_list_node = []
        while head:
            new_list_node.append(head)
            head = head.next
        if len(new_list_node) == 1:
            return None
        if len(new_list_node)-n != 0:

            new_list_node[len(new_list_node)-n-1].next = new_list_node[len(new_list_node)-n].next
        
        new_list_node.remove(new_list_node[len(new_list_node)-n])
        #print(new_list_node)
        current = ListNode()
        new = current
        for each in range(len(new_list_node)):
            current.next = new_list_node[each]
            
            #print(new_list_node[each])
            current = current.next
        return new.next
        
        