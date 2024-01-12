# 953. Verifying an Alien Dictionary
# Solved
# Easy
# Topics
# Companies
# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        hash_map = {}
        for each in range(len(order)):
            hash_map[order[each]] = each
        for each in range(len(words)-1):
            r = each + 1
            while r < len(words):
                len_word = min(len(words[each]), len(words[r]))
                i = 0
                while i < len_word:
                    #if words[each][i] != words[r][i]:
                    if hash_map[words[each][i]] > hash_map[words[r][i]]:
                        return False
                    #elif hash_map[words[each][i]] == hash_map[words[r][i]]:

                    elif hash_map[words[each][i]] < hash_map[words[r][i]]:
                        break
                    i += 1
                if len(words[each]) > len(words[r]) and words[each].startswith(words[r]):
                    return False
                r+=1
            
        return True

        