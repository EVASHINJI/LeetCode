# Url: https://leetcode.com/problems/multiply-strings/
# Related Topics:
# String Math

# Example:
# Input: num1 = "123", num2 = "456"
# Output: "56088"


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        i, j = 0, 0
        l1, l2 = len(num1), len(num2)
        num1 = [int(c) for c in num1[::-1]]
        num2 = [int(c) for c in num2[::-1]]
        ans = [0] * (l1 + l2)
        for i in range(l1):
            for j in range(l2):
                ans[i+j] += num1[i] * num2[j]
        for i in range(l1 + l2):
            if ans[i] >= 10:
                ans[i+1] += ans[i] // 10
                ans[i] = ans[i] % 10
            ans[i] = str(ans[i])
        return ''.join(reversed(ans)).lstrip('0')