# 50. Pow(x, n)
# Solved
# Medium
# Topics
# Companies
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # if n == 0:
        #     return 1
        # if x == 0:
        #     return 0
        # if n > 0:
        #     if n %2 == 0:
        #         return self.myPow(x,n//2) * self.myPow(x,n//2) 
        #     else:
        #         return self.myPow(x,n//2) * self.myPow(x,n//2) * x
        # elif n < 0:
        #     n = -n
        #     if n %2 == 0:
        #         return 1/(self.myPow(x,n//2) * self.myPow(x,n//2) )
        #     else:
        #         return 1/ (self.myPow(x,n//2) * self.myPow(x,n//2) * x)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n > 0:
            half_pow = self.myPow(x, n // 2)
            return half_pow * half_pow if n % 2 == 0 else half_pow * half_pow * x
        else:  # n < 0
            n = -n
            half_pow = self.myPow(x, n // 2)
            return 1 / (half_pow * half_pow) if n % 2 == 0 else 1 / (half_pow * half_pow * x)

