# Url: https://leetcode.com/problems/binary-gap/
# Related Topics:
# Math

# Example:
# Input: 22
# Output: 2


class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans, pos = 0, -1
        for i, c in enumerate(str(bin(N))[2:]):
            if c == '1':
                if pos >= 0 and i - pos > ans:
                    ans = i - pos
                pos = i
        return ans