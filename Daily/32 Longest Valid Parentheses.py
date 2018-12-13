# Url: https://leetcode.com/problems/longest-valid-parentheses/
# Related Topics:
# String DP

# Example:
# Input: ")()())"
# Output: 4


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, seq = [], list(s)
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif stack:
                j = stack.pop()
                seq[i], seq[j] = '1', '1'
                
        ans, i = 0, 0
        while i < len(seq):
            tmp = 0
            while i < len(seq) and seq[i] == '1':
                tmp += 1
                i += 1
            i += 1
            ans = max(ans, tmp)
        return ans