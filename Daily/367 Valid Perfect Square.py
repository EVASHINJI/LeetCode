# Url: https://leetcode.com/problems/valid-perfect-square/
# Related Topics:
# Math BinarySearch

# Example:
# Input: 16
# Output: true


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        lo, hi = 1, num
        while lo <= hi:
            mid = (lo + hi) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return False