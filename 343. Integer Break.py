# 343. Integer Break
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

# Return the maximum product you can get.

 

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# Example 2:

# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
 

# Constraints:

# class Solution(object):
#     def integerBreak(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
        
#         def dfs(num):
            
#             if num == 1:
#                 return 1
#             result = 0
#             for i in range(1,num):
#                 result = max(result, i * (num-i), dfs(i) * dfs(num - i), i * dfs(num - i))
            
#             return result
#         return dfs(n)
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}

        def dfs(num):
            if num == 1:
                return 1

            if num in memo:
                return memo[num]

            result = 0
            for i in range(1, num):
                # Calculate the product for three cases: 
                # 1. No break: i * (num - i)
                # 2. Break only the first part: i * dfs(num - i)
                # 3. Break only the second part: dfs(i) * (num - i)
                result = max(result, i * (num - i), i * dfs(num - i), dfs(i) * (num - i))

            memo[num] = result
            return result

        return dfs(n)





