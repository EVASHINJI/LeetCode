# Url: https://leetcode.com/problems/rectangle-area/
# Related Topics:
# Math

# Example:
# Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
# Output: 45


class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area = (C-A)*(D-B) + (G-E)*(H-F)
        X = sorted([A, C, E, G])
        Y = sorted([B, D, F, H])
        if (A <= X[1] < C or E <= X[1] < G) and (B <= Y[1] < D or F <= Y[1] < H):
            area -= (X[2] - X[1]) * (Y[2] - Y[1])
        return area