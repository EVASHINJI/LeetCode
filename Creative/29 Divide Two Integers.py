# Url: https://leetcode.com/problems/divide-two-integers/
# Related Topics:
# Math BinarySearch

# Example:
# Input: dividend = 7, divisor = -3
# Output: -2

# Creative
# BinarySearch. Find the regular and skip it.


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        while dividend >= divisor:
            tmp, i = divisor, 1
            while dividend >= tmp:
                dividend -= tmp
                ans += i
                tmp = tmp << 1
                i = i << 1
        if neg:
            ans = -ans
        return min(max(-2147483648, ans), 2147483647)