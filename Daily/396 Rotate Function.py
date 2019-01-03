# Url: https://leetcode.com/problems/rotate-function/submissions/
# Related Topics:
# Math

# Example:
# A = [4, 3, 2, 6]
# F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
# F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
# F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
# F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
# So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.


class Solution:
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        total, l = sum(A), len(A)
        ma = cur = sum([a*i for i, a in enumerate(A)])
        for i in range(l - 1):
            cur = cur - total + A[i]*l
            if cur > ma:
                ma = cur
        return ma