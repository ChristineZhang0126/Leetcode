# 680. Valid Palindrome II
# Solved
# Easy
# Topics
# Companies
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s)-1
        temp = s
        left_time = True
        right_time = True
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                break
        if l == r or l - r == 1:
            return True
        s = s[:l] + s[l+1:]
        left = 0
        right = len(s) - 1
       # print(s)
        while left < right:
            if s[left] != s[right] :
                left_time = False
                break
            left += 1
            right -= 1
        
        temp = temp[:r] + temp[r+1:]
        #print(temp)
        left = 0
        right = len(temp) - 1
        while left < right:
            if temp[left] != temp[right] :
                right_time = False
                break
            left += 1
            right -= 1
        if not left_time and not right_time:
            return False
        else:
            return True

