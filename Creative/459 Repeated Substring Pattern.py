# Url: https://leetcode.com/problems/repeated-substring-pattern/
# Related Topics:
# String

# Example:
# Input: "abcabcabcabc"
# Output: True

# Creative construct loop body


class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = (s*2)[1:-1]
        return s in a