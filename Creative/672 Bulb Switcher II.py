# Url: https://leetcode.com/problems/bulb-switcher-ii/
# Related Topics:
# Math

# Example:
# Input: n = 3, m = 1.
# Output: 4
# Explanation: Status can be: [off, on, off], [on, off, on], [off, off, off], [off, on, on].

# Creative
# find the real changed part


class Solution:
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        n = min(n, 3)
        if m == 0: return 1
        if m == 1: return [2, 3, 4][n-1]
        if m == 2: return [2, 4, 7][n-1]
        return [2, 4, 8][n-1]