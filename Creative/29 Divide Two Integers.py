# Url: https://leetcode.com/problems/fraction-to-recurring-decimal/
# Related Topics:
# Math BinarySearch

# Example:
# Input: dividend = 7, divisor = -3
# Output: -2

# Creative
# BinarySearch. Find the regular and skip it.


class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator*denominator < 0 else ''
        result = [sign+str(n), '.']
        stack = []
        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(n))

        idx = stack.index(remainder)
        result.insert(idx+2, '(')
        result.append(')')
        return ''.join(result).replace('(0)', '').rstrip('.')