# Url: https://leetcode.com/problems/valid-parentheses/
# Related Topics:
# String Stack

# Example:
# Input: "()[]{}"
# Output: true


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            elif not stack or mapping[stack.pop()] != c:
                return False
        if stack:
            return False
        return True