# Url: https://leetcode.com/problems/reverse-words-in-a-string/
# Related Topics:
# String

# Example:
# Input: "the sky is blue",
# Output: "blue is sky the".


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])