# 424. Longest Repeating Character Replacement
# Medium
# 9.9K
# 446
# Companies
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # two pointer sliding window
        # hashmap
        # len(window) - most_freq element in the window <= k
        # result is the len of the indow
        new_hash = {}
        l = 0
        for r in range(len(s)):
            if s[r] not in new_hash:
                new_hash[s[r]] = 1
            else:
                new_hash[s[r]] += 1
            if ((r-l+1) - max(new_hash.values())) > k:
                new_hash[s[l]] -= 1
                l+=1
        return (r-l+1)
        