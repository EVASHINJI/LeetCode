# Url: https://leetcode.com/problems/valid-parenthesis-string/
# Related Topics:
# String

# Example:
# Input: "(*))"
# Output: True

# Creative use lo hi represent the potential range of balance of the parenthesis


class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lo, hi = 0, 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0:
                break
            lo = max(lo, 0)
        return lo == 0