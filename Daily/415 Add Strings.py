# Url: https://leetcode.com/problems/add-strings/
# Related Topics:
# Math

# Example:
# Input: "55555555550", "55555555557"
# Output: "111111111107"


class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1, l2 = len(num1), len(num2)
        l = max(l1, l2)
        num1, num2 = num1[::-1], num2[::-1]
        plus = 0
        ans = ''
        for i in range(l):
            n1 = int(num1[i]) if i < l1 else 0
            n2 = int(num2[i]) if i < l2 else 0
            plus, cur = divmod(n1+n2+plus, 10)
            ans += str(cur)
        if plus:
            ans += str(plus)
        return ans[::-1]