# Url: https://leetcode.com/problems/factorial-trailing-zeroes/
# Related Topics:
# Math

# Example:
# Input: 5
# Output: 1


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)