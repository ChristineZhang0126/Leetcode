# 91. Decode Ways
# Medium
# 11.5K
# 4.5K
# Companies
# A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it.

# The test cases are generated so that the answer fits in a 32-bit integer.

 
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # every time we add one more,
        # we have two ways: number of way add it single digit(not 0)  that is dp[n-1]  plus dp[n-2]*(number of ways to construct n-1 and n)    
        dp = []
        for each in range(len(s)+1):
            dp.append(0)
        if len(s)==0:
            return 0
        elif len(s)== 1 and s == '0':
            return 0
        elif len(s) == 1 and 1 <= int(s) <= 9:
            return 1
        elif s[0] == '0':
            return 0
        else:
            dp[0] = 1
            dp[1] = 1
            for i in range(1,len(s)):
                if 1<= int(s[i]) <= 9 and s[i-1] == '0':
                   dp[i+1] = dp[i]
                elif 1<= int(s[i]) <= 9 and 1 <= int (s[i-1] + s[i]) <= 26:
                    dp[i+1] = dp[i] + dp[i-1]
                elif 1<= int(s[i]) <= 9 and 27 <= int (s[i-1] + s[i]) <= 99:
                    dp[i+1] = dp[i]
                elif int(s[i]) == 0 and s[i-1] == '0' or (int(s[i]) == 0 and int(s[i-1]) > 2) :
                    return 0
                elif int(s[i]) == 0 and int(s[i-1]) <= 2:
                    dp[i+1] = dp[i-1]
        return dp[len(s)]