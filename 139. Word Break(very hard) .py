# 139. Word Break (very hard)
# Medium
# 16.6K
# 726
# Companies
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
 

# Constraints:

# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # # dp each charater what the word can be formed in that character
        # 39/46 test cases passed
        # l = 0
        # another_l = 0
        # for each in range(len(s)):
        #     if s[l:each+1] in wordDict:
        #         l = each + 1
        # print(l)

        # for each in range(len(s)):
            
        #     if s[another_l:each+1] in wordDict:
        #         if each + 2 <= len(s):
        #             #print(s[l:each+2])
        #             if s[another_l:each+2] in wordDict:
                        
        #                 another_l = each + 2
        #             else:
        #                 another_l = each+1
        #         else:
        #             another_l = each + 1
        #     #print(another_l)
        # print(another_l)
    
        
        # if l == (len(s)) or another_l == len(s):
        #     return True
        # else:
        #     return False
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]
