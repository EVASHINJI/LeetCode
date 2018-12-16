# Url: https://leetcode.com/problems/power-of-three/
# Related Topics:
# Math

# Example:
# Input: 27
# Output: true


class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n != 0:
            if n == 1:
                return True
            n, m = divmod(n, 3)
            if m:
                return False
        return False
            