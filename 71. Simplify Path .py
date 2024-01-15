# 71. Simplify Path
# Solved
# Medium
# Topics
# Companies
# Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

# In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

# The canonical path should have the following format:

# The path starts with a single slash '/'.
# Any two directories are separated by a single slash '/'.
# The path does not end with a trailing '/'.
# The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
# Return the simplified canonical path.

 

# Example 1:

# Input: path = "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory name.
# Example 2:

# Input: path = "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
# Example 3:

# Input: path = "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

 class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        return_list = []
        return_str = ''
        l = 0
        r = 1

        while r < len(path):
            #len_add = 0     
            if path[r] != '/':
                r += 1
            elif path[r] == "/" and (r-l) != 1:
                stack.append(path[l+1:r])
                l = r
                r += 1
            elif path[r] == "/" and (r-l) == 1:
                r += 1
                l += 1
        if (r - l) != 1:
            stack.append(path[l+1:r])
        print(stack)
        for i in stack:
            if i != "." and i != "..":
                return_list.append(i)
            elif i == '..':
                if return_list:
                    return_list.pop()
        if not return_list:
            return'/'
        for each in return_list:
            return_str +=  "/" + each
        return return_str

            
        

            


            