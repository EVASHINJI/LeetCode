# Url: https://leetcode.com/problems/powx-n/
# Related Topics:
# Math BinarySearch

# Example:
# Input: 2.10000, 3
# Output: 9.26100

# Creative
# BinarySearch


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow