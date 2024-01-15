# 791. Custom Sort String
# Solved
# Medium
# Topics
# Companies
# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.

 

# Example 1:

# Input: order = "cba", s = "abcd"
# Output: "cbad"
# Explanation: 
# "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
# Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
# Example 2:

# Input: order = "cbafg", s = "abcd"
# Output: "cbad"
class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        new_hash = {}
        for each in range(len(order)):
            new_hash[each] = str(order[each])
        another_hash = {}
        for i in range(len(s)):
            if s[i] not in new_hash.values():
                if len(order) not in another_hash:
                    another_hash[len(order)] = [str(s[i])]
                else:
                    another_hash[len(order)].append(s[i])
                # if s[i] not in another_hash.values():
                #     print("sdfsdfsdf")
                #     another_hash[len(order)] = [str(s[i])]
                # elif s[i] in another_hash.values():
                #     another_hash[len(order)].append(str(s[i]))
            elif s[i] in new_hash.values():
                for key,value in new_hash.items():
                    if value == s[i]:
                        if key not in another_hash:
                            another_hash[key] = [str(s[i])]
                        else:
                            another_hash[key].append(str(s[i]))

        the_list = []
        the_str = ''
        print(another_hash)
        for each in another_hash:
            the_list.append(each)
        heapq.heapify(the_list)
        while the_list:
            the_pop = heapq.heappop(the_list)
            for each in another_hash[the_pop]:
                the_str += each
        return the_str



            