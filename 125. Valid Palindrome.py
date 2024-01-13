# 125. Valid Palindrome
# Solved
# Easy
# Topics
# Companies
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new = list(str(s))
        another = ''
        for each in range(len(new)):
            if not new[each].isalpha() and not new[each].isdigit():
                new[each] = ''
                #new.remove(new[each])
            #elif not new[each].
            elif new[each].isupper():
                new[each] = new[each].lower()
            another += new[each]
        #if len(another) == 1:
            #return False
        l = 0
        r = len(another) - 1
        # #print(new)
        
        while l != r and l < r:
            if another[l] != another[r]:
                return False
            l +=1
            r-=1
        return True
            
            



