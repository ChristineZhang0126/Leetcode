# 242. Valid Anagram
# Easy
# 11.5K
# 364
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
 
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        first_hash = {}
        second_hash = {}
        for each in s:
            if each not in first_hash:
                first_hash[each] = 1
            else:
                first_hash[each] += 1
        for each in t:
            if each not in second_hash:
                second_hash[each] = 1
            else:
                second_hash[each] += 1
        if len(s) != len(t):
            return False
        else:
            for i in first_hash:
                if i not in second_hash:
                    return False
                elif i in second_hash:
                    if first_hash[i] != second_hash[i]:
                        return False
        return True