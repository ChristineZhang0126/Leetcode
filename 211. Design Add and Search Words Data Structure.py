# 211. Design Add and Search Words Data Structure
# Solved
# Medium
# Topics
# Companies
# Hint
# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

# Example:

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
class Node(object):
    def __init__(self):
        self.children = {}
        self.endofword = False

class WordDictionary(object):

    def __init__(self):
        self.root = Node()

        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for each in word:
            if each not in cur.children:
                cur.children[each] = Node()
            cur = cur.children[each]
        cur.endofword = True

        

    # def search(self, word):
    #     """
    #     :type word: str
    #     :rtype: bool
    #     """
        # cur = self.root
        # for each in range(len(word)):
        #     if word[each] != ".":
        #         if word[each] not in cur.children:
        #             return False
        #         else:
        #             cur = cur.children[str(word[each])]
        #     elif word[each] == ".":
        #         for word[each] in cur.children:
        #             if self.search(word[each:]):
        #                 return True
        #         return False
        #     cur = cur.children[str(word[each])]
        #return False
    def search_helper(self, word, node):
        cur = node
        for char in range(len(word)):
            if word[char] != ".":
                if word[char] not in cur.children:
                    return False
                else:
                    cur = cur.children[word[char]]
            elif word[char] == ".":
                for child in cur.children:
                    if self.search_helper(word[char + 1:], cur.children[child]):
                        return True
                return False
        return cur.endofword

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.search_helper(word, self.root)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
            



