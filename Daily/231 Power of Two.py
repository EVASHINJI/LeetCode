# Url: https://leetcode.com/problems/power-of-two/
# Related Topics:
# Math

# Example:
# Input: 16
# Output: true


class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n != 1:
            n, m = divmod(n, 2)
            if m == 1:
                return False
        return True