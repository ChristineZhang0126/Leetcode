# 567. Permutation in String
# Medium
# 11K
# 370
# Companies
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
# class Solution(object):
#     def checkInclusion(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
#         # permutation algorithm
#         def backtrack(start, end):
#             if start == end:
#                 permutations.append(''.join(current_permutation))
#                 return

#             for i in range(start, end):
#                 # Swap characters at positions start and i
#                 current_permutation[start], current_permutation[i] = current_permutation[i], current_permutation[start]

#                 # Recursively generate permutations for the remaining characters
#                 backtrack(start + 1, end)

#                 # Backtrack: Undo the swap for backtracking
#                 current_permutation[start], current_permutation[i] = current_permutation[i],current_permutation[start]

#         permutations = []
#         current_permutation = list(s1)
#         backtrack(0, len(s1))
#         for each in permutations:
#             if each in s2:
#                 return True
#         return False

class Solution(object):
    def checkInclusion(self, s1, s2):
        new_hash = {}
        another_hash = {}
        for each in s1:
            if each not in new_hash:
                new_hash[str(each)] = 1
            else:
                new_hash[str(each)] += 1
        #print(new_hash)
     
        for i in range(len(s2) - len(s1) + 1):
            for index in s2[i:i+len(s1)]:
                if index not in another_hash:
                    another_hash[str(index)] = 1
                    
                else:
                    another_hash[str(index)] += 1
               # print(another_hash)
                #print(new_hash == another_hash)
            if new_hash == another_hash:
                return True
            another_hash = {}
        return False
