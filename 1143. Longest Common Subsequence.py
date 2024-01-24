# 1143. Longest Common Subsequence
# Solved
# Medium
# Topics
# Companies
# Hint
# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
 # class Solution(object):
#     def longestCommonSubsequence(self, text1, text2):
#         """
#         :type text1: str
#         :type text2: str
#         :rtype: int
#         """
#         return_list = [0] * max(len(text1),len(text2))
#         pointer_text1 = 0
#         pointer_text2 = 0
#         while pointer_text1 < len(text1) and pointer_text1 < len(text2):
#             if text1[pointer_text1] != text2[pointer_text2]:
#                 if len(return_list) == len(text1):
#                     return_list[pointer_text1] = return_list[pointer_text1-1]
#                     pointer_text1 += 1
#                     #return_list
#                 elif len(return_list) == len(text2):
#                     return_list[pointer_text2] = return_list[pointer_text2-1]
#                     pointer_text2 += 1
                
#             else:
#                 if len(return_list) == len(text1):
#                     #return_list[pointer_text1][0] = True
#                     return_list[pointer_text1] = return_list[pointer_text1-1] + 1

#                 elif len(return_list) == len(text2):
#                     #return_list[pointer_text2][0] = True
#                     return_list[pointer_text2] = return_list[pointer_tex2-1] + 1
#                 pointer_text1 += 1
#                 pointer_text2 += 1
#         print(return_list)
#         return max(return_list)
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m, n = len(text1), len(text2)

        # Initialize a 2D array for dynamic programming
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Iterate over the characters of text1 and text2
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The result is stored in the bottom-right cell of the dp array
        return dp[m][n]

# Example usage:
sol = Solution()
text1_1, text2_1 = "abcde", "ace"
text1_2, text2_2 = "abc", "abc"

result_1 = sol.longestCommonSubsequence(text1_1, text2_1)
result_2 = sol.longestCommonSubsequence(text1_2, text2_2)

print(result_1)  # Output: 3
print(result_2)  # Output: 3

            

        
