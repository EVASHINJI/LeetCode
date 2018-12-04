# Url: https://leetcode.com/problems/valid-palindrome/
# Related Topics:
# String TwoPointers

# Example:
# Input: "A man, a plan, a canal: Panama"
# Output: true


import re
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub('[^a-z0-9]+', '', s.lower())
        return s == s[::-1]