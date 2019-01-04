# Url: https://leetcode.com/problems/water-and-jug-problem/
# Related Topics:
# Math

# Example:
# Input: x = 3, y = 5, z = 4
# Output: True

# Bézout's identity 裴蜀定理


class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a%b)
        
        return z == 0 or (x + y >= z and z % gcd(x, y) == 0)