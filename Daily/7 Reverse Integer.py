# Url: https://leetcode.com/problems/reverse-integer/
# Related Topics:
# Math

# Example:
# Input: -123
# Output: -321


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        def in_range(x):
            if x < -(2**31) or x > 2**31 - 1:
                return 0
            return 1

        sign = -1 if x < 0 else 1
        x, ans = abs(x), 0
        while x != 0:
            x, m = divmod(x, 10)
            ans = ans*10 + m
        return sign*ans*in_range(sign*ans)