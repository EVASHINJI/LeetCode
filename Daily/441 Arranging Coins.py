# Url: https://leetcode.com/problems/arranging-coins/
# Related Topics:
# Math BinarySearch

# Example:
# Input: 8
# Output: 3


class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 0, n
        while lo <= hi:
            mid = (lo + hi) // 2
            num = mid * (mid + 1) / 2
            if n == num:
                return mid
            if n > num:
                if n - num <= mid:
                    return mid
                lo = mid + 1
            else:
                hi = mid - 1
        return -1