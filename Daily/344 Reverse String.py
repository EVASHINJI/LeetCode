# Url: https://leetcode.com/problems/reverse-string/
# Related Topics:
# String

# Example:
# Input: "A man, a plan, a canal: Panama"
# Output: "amanaP :lanac a ,nalp a ,nam A"

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]