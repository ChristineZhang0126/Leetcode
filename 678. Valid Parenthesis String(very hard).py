# 678. Valid Parenthesis String
# Solved
# Medium
# Topics
# Companies
# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

# The following rules define a valid string:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "(*)"
# Output: true
# Example 3:

# Input: s = "(*))"
# Output: true
# class Solution(object):
#     def checkValidString(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         l = 0
#         r = len(s) - 1
#         #the_list = list(s)
#         if '*' not in s:
#             if len(s) % 2 != 0:
#                 return False
#             else:
                
#                 # two pointers
                
#                 while s[r] == ')' and l < r:
#                     if s[l] == '(':
#                         l += 1
#                         r -= 1
#                     else:
#                         return False
#                 if l < r:
#                     return False
#         else:
#             while l < r:
#                 if s[l] == '(' or '*':
#                         l += 1
#                         r -= 1
#                 else:
#                     return False
#             if len(s) % 2 != 0:
#                 if s[l] != '*':
#                     return False

#         return True
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        max_open, min_open = 0, 0

        for c in s:
            # if c == '(': min_open += 1 
            # else: min_open -=1
            min_open = min_open + 1 if c == '(' else min_open - 1
            max_open = max_open + 1 if c != ')' else max_open - 1

            if max_open < 0: return False
            min_open = max(0, min_open)

        return min_open == 0