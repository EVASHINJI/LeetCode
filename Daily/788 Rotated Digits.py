# Url: https://leetcode.com/problems/rotated-digits/
# Related Topics:
# String

# Example:
# Input: 10
# Output: 4


class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        valid = {'0', '1', '8', '2', '5', '6', '9'}
        good = {'2', '5', '6', '9'}
        cnt = 0
        for i in range(1, N+1):
            num = str(i)
            if '3' in num or '4' in num or '7' in num:
                continue
            if '2' in num or '5' in num or '6' in num or '9' in num:
                cnt += 1
        return cnt
        