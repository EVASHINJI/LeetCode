# Url: https://leetcode.com/problems/reverse-string-ii/
# Related Topics:
# String

# Example:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"


class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) <= k:
            return s[::-1]
        return s[k-1::-1] + s[k: 2*k] + self.reverseStr(s[2*k:], k)