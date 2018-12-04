# Url: https://leetcode.com/problems/length-of-last-word/
# Related Topics:
# String

# Example:
# Input: "Hello World"
# Output: 5


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1])