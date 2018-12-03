# Url: https://leetcode.com/problems/reverse-only-letters/
# Related Topics:
# String

# Example:
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"

# Creative Use Stack to Reve


class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = [s for s in S if s.isalpha()]
        ans = []
        for s in S:
            if s.isalpha():
                ans.append(stack.pop())
            else:
                ans.append(s)
        return ''.join(ans)