# Url: https://leetcode.com/problems/palindrome-number/
# Related Topics:
# Math

# Example:
# Input: 121
# Output: true


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        return s == s[::-1]