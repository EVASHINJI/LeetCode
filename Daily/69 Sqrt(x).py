# Url: https://leetcode.com/problems/sqrtx/
# Related Topics:
# Math BinarySearch

# Example:
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
#              the decimal part is truncated, 2 is returned.


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        lo, hi = 1, x
        while True:
            mid = int((lo+hi)/2)
            if mid*mid <= x < (mid+1)**2:
                return mid
            if mid*mid > x:
                hi = mid - 1
            else:
                lo = mid + 1
        