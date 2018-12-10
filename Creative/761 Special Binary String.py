# Url: https://leetcode.com/problems/special-binary-string/
# Related Topics:
# String Recursion

# Example:
# Input: S = "11011000"
# Output: "11100100"

# Creative Think of it as Valid-Parentheses


class Solution:
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        balance, i = 0, 0
        res = []
        for k, c in enumerate(S):
            balance += 1 if c == '1' else -1
            if balance == 0:
                res.append('1' + self.makeLargestSpecial(S[i+1: k]) + '0')
                i = k + 1
        return ''.join(sorted(res, reverse=True))