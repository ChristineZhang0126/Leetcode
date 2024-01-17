# 2055. Plates Between Candles
# Solved
# Medium
# Topics
# Companies
# Hint
# There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

# You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

# For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.
# Return an integer array answer where answer[i] is the answer to the ith query.

 

# Example 1:

# ex-1
# Input: s = "**|**|***|", queries = [[2,5],[5,9]]
# Output: [2,3]
# Explanation:
# - queries[0] has two plates between candles.
# - queries[1] has three plates between candles.
# Example 2:

# ex-2
# Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
# Output: [9,0,0,0,0]
# Explanation:
# - queries[0] has nine plates between candles.
# - The other queries have zero plates between candles.
# # class Solution(object):
# #     def platesBetweenCandles(self, s, queries):
# #         """
# #         :type s: str
# #         :type queries: List[List[int]]
# #         :rtype: List[int]
# #         """
# #         return_list = []
# #         stack = []
# #         for each in range(len(queries)):
# #             num = 0
# #             for i in s[queries[each][0]:queries[each][1]+1]:
# #                 if not stack and i == '|':
# #                     stack.append("|")
# #                 elif stack and stack[-1] == "*" and i == '|':
# #                     #print(len(stack))
# #                     index = len(stack) - 1
# #                     while stack[index] == "*" :
# #                         stack.pop()
# #                        # print("sdfsdf")
# #                         num += 1
# #                         index -= 1
# #                 elif i == '*' and stack:
# #                     stack.append("*")
# #                     #print("sdfsdfsdfsd")
# #             return_list.append(num)
# #             stack = []
# #         return return_list

# class Solution(object):
#     def platesBetweenCandles(self, s, queries):
#         return_num = []
#         for each in range(len(queries)):
            
#             left = queries[each][0]
#            # right = queries[each][0] + 1
#             while s[left] == "*":
#                 left += 1
#             right = left + 1
#             num = 0
#             while right <= queries[each][1]:
#                 if s[right] == "*" :
#                     right += 1
#                 elif s[right] == s[left] and right - left != 1:
#                     num += right - left - 1
#                     left = right
#                     right = left + 1
#                 elif s[right] == s[left] and right - left == 1:
#                     left = right
#                     right = left + 1
                    
#                 else:
#                     right += 1
#             return_num.append(num)
#         return return_num
class Solution(object):
    def platesBetweenCandles(self, s, queries):
        A = [i for i,c in enumerate(s) if c == '|']
        res = []
        for a,b in queries:
            i = bisect.bisect_left(A, a)
            j = bisect.bisect(A, b) - 1
            res.append((A[j] - A[i]) - (j - i) if i < j else 0)
        return res