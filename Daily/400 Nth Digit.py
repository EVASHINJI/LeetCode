# Url: https://leetcode.com/problems/nth-digit/
# Related Topics:
# Math

# Example:
# Input: 11
# Output: 0
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.


class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n
        total, base, digit = 0, 9, 1
        while total + digit*base < n:
            total += digit*base
            digit += 1
            base *= 10
        
        d, m = divmod(n - total - 1, digit)
        num = 10 ** (digit-1) + d
        return int(str(num)[m])
        
        