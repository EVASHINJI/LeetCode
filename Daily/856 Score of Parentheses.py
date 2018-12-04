# Url: https://leetcode.com/problems/score-of-parentheses/
# Related Topics:
# String Stack

# Example:
# Input: "(()(()))"
# Output: 6


class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for c in S:
            if c == '(':
                stack.append(c)
            else:
                score = 0
                last = stack.pop()
                while last != '(':
                    score += int(last)
                    last = stack.pop()
                score = score * 2 if score else 1
                stack.append(score)
        return sum(stack)
                    