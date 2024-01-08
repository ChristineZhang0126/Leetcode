# 2272. Substring With Largest Variance
# Hard
# 1.8K
# 205
# Companies
# The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.

# Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: s = "aababbb"
# Output: 3
# Explanation:
# All possible variances along with their respective substrings are listed below:
# - Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
# - Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
# - Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
# - Variance 3 for substring "babbb".
# Since the largest possible variance is 3, we return it.
# Example 2:

# Input: s = "abcde"
# Output: 0
# Explanation:
# No letter occurs more than once in s, so the variance of every substring is 0.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.
# class Solution(object):
#     def largestVariance(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         # brute force
#         # iterate every substring, use a hashmap to calculate the occurance
#         max_occur = 0

#         for each in range(len(s)-1):
#             for i in range(each + 1, len(s)):
#                 new_hash = {}
#                 #if s[each:i+1] == "babbb":
#                    # print("sdf")
#                 for all_char in s[each:i+1]:
#                     if all_char not in new_hash:
#                         new_hash[all_char] = 1
#                     else:
#                         new_hash[all_char] += 1
#                 #print(s[each:i])
#                 max_diff = max(new_hash.values()) - min(new_hash.values())
#                 #print(max_diff)
#                 max_occur = max(max_occur, max_diff)
#                 #print(max_occur)
#         return max_occur

class Solution(object):
    def largestVariance(self, s):
        counter = collections.Counter(s)
        res = 0
        for char1, char2 in itertools.combinations(counter, 2):
            char1_count = counter[char1]
            char2_count = counter[char2]
            diff = 0
            seen_char1 = seen_char2 = False
            for char in s:
                if char not in (char1, char2):
                    continue
                if diff < 0:
                    if not char1_count :
                        break
                    if not char2_count:
                        res = max(res,diff + char1_count)
                        break
                    seen_char1 = seen_char2 = False
                    diff = 0
                    if char == char1:
                        seen_char1 = True
                        char1_count -= 1
                        diff +=1
                    if char == char2:
                        seen_char2 = True
                        char2_count -= 1
                        diff -=1
                    if seen_char1 and seen_char2:
                        res = max(res,diff)
        return res
            

        