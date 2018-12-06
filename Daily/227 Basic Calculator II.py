# Url: https://leetcode.com/problems/basic-calculator-ii/
# Related Topics:
# String

# Example:
# Input: "3+2*2"
# Output: 7


class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += '+'
        n, sign = 0, '+'
        stack = []
        for c in s:
            if c.isdigit():
                n = 10*n + ord(c) - 48
            elif c != ' ':
                if sign == '+':
                    stack.append(n)
                if sign == '-':
                    stack.append(-n)
                if sign == '*':
                    stack.append(stack.pop() * n)
                if sign == '/':
                    stack.append(int(stack.pop() / n))
                n = 0
                sign = c
        return sum(stack)