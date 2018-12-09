# Url: https://leetcode.com/problems/simplify-path/
# Related Topics:
# String Stack

# Example:
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# path = "/a/../../b/../c//.//", => "/c"
# path = "/a//b////c/d//././/..", => "/a/b/c"


class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dictionary = path.split('/')
        ans = []
        for d in dictionary:
            if d == '.' or d == '':
                continue   
            if d != '..':
                ans.append(d)
            elif ans:
                ans.pop()
            
        return '/' + '/'.join(ans)