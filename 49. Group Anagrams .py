# 49. Group Anagrams
# Medium
# 17.9K
# 537
# Companies
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sort_array = {}
        for each in range(len(strs)):
            
            if ''.join(sorted(strs[each])) not in sort_array:
                #print(''.join(sorted(strs[each])))
                
                
                new_string = ''.join(sorted(strs[each]))
                #print(strs[each])
                
                sort_array[str(new_string)] = [str(strs[each])]
                #print(sort_array[new_string])
                #print(sort_array[''.join(sorted(strs[each]))])

            else:
                another_str = ''.join(sorted(strs[each]))
                sort_array[str(another_str)].append(str(strs[each]))
               # print(sort_array[''.join(sorted(strs[each]))])
      
        #print(sort_array.items())
        return list(sort_array.values())

        
        