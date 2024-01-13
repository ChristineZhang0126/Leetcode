# 1249. Minimum Remove to Make Valid Parentheses
# Solved
# Medium
# Topics
# Companies
# Hint
# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 

# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:

# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        invalid_index = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
                invalid_index.append(i)
            elif s[i] == ")":
                if not stack:
                    invalid_index.append(i)
                if stack:
                    stack.pop()
                    invalid_index.pop()
        new_str = ''
        for each in range(len(s)):
            if each in invalid_index:
                continue
            else:
                new_str = new_str + s[each]
        return new_str



