# Url: https://leetcode.com/problems/to-lower-case/
# Related Topics:
# String

# Example 1:
# Input: "Hello"
# Output: "hello"


class Solution:
    def toLowerCase(self, str1):
        """
        :type str: str
        :rtype: str
        """
        return ''.join([chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in str1])