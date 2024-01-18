# 767. Reorganize String
# Solved
# Medium
# Topics
# Companies
# Hint
# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

 

# Example 1:

# Input: s = "aab"
# Output: "aba"
# Example 2:

# Input: s = "aaab"
# Output: ""
 

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # new_hash = {}
        # return_string = ""
        # for each in range(len(s)):
        #     if s[each] not in new_hash:
        #         new_hash[s[each]] = 1
        #     else:
        #         new_hash[s[each]] += 1
        # if max(new_hash.values()) - min(new_hash.values()) >= 2:
        #     return return_string
        # else:
        #     while new_hash.values() != [0] * len(new_hash.values()):
        #         for each in new_hash:
        #             if new_hash[each] != 0:
        #                 return_string += each
        #                 new_hash[each] -= 1
class Solution:
    def reorganizeString(self, s):
        count = Counter(s)  # Hashmap, count each char
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)  # O(n)

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            # most frequent, except prev
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return res