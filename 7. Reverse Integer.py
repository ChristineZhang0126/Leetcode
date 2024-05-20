# 7. Reverse Integer
# Solved
# Medium
# Topics
# Companies
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1
import math

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MIN = -2147483648  # -2^31
        MAX = 2147483647  # 2^31 - 1

        res = 0
        negative = x < 0
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            x = x // 10
            
            # Check for overflow before updating res
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            
            res = res * 10 + digit
        
        if negative:
            res = -res
        
        # Final check for overflow
        if res < MIN or res > MAX:
            return 0
        
        return res
        