# 5. Longest Palindromic Substring
# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # if len(s) == 1:
        #     return s
        
        # longest_word = ''

        # for each in range(len(s)):
        #     for i in range(each+1,len(s)):
        #         #is_palin = False
        #         l = each
        #         r = i
        #         while l < r and l != r:
        #             if s[l] == s[r]:
        #                 l+=1
        #                 r-=1
        #             else:
        #                 break
                
        #         #if len(s[each:i+1]) % 2 == 0:
        #         if l - r == 1:
        #             if len(s[each:i+1]) > len(longest_word):
        #                 longest_word = s[each:i+1]
                        
        #         elif l == r:
        #             if len(s[each:i+1]) > len(longest_word):
        #                 longest_word = s[each:i+1]
        # if longest_word == '':
        #     longest_word = s[0]
                       
        #                 #print(s[each:i])
        # return longest_word
        # dp
        # what is the longest palindromic string for each character in
        # the string that the character is the center of the palindrone
        longest_word = ''
        # even len
        for each in range(len(s)):
            l = each
            r = each
            while l >=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            if (r-l+1) > len(longest_word):
                longest_word = s[l:r+1]
        # odd len
        for each in range(len(s)):
            l = each
            r = each + 1
            while l >=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            if (r-l+1) > len(longest_word):
                longest_word = s[l:r+1]
        return longest_word
            

        
        