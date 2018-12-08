# Url: https://leetcode.com/problems/remove-comments/
# Related Topics:
# String

# Example:
# Input: 
# source = ["a/*comment", "line", "more_comment*/b"]
# Output: ["ab"]


class Solution:
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        in_block = False
        ans = []
        for line in source:
            if not in_block:
                newline = []
            i = 0
            while i < len(line):
                if line[i:i+2] == '/*' and not in_block:
                    in_block = True
                    i += 1
                elif line[i:i+2] == '*/' and in_block:
                    in_block = False
                    i += 1
                elif not in_block and line[i:i+2] == '//':
                    break
                elif not in_block:
                    newline.append(line[i])
                i += 1
            if newline and not in_block:
                ans.append(''.join(newline))
        
        return ans
            