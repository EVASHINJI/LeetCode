# Url: https://leetcode.com/problems/mirror-reflection/
# Related Topics:
# Math

# Example:
# Input: p = 2, q = 1
# Output: 2
# Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.


class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        g = gcd(p, q)
        p = (p / g) % 2
        q = (q / g) % 2
        return 1 if p and q else 0 if p else 2
            