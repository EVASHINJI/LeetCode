# Url: https://leetcode.com/problems/smallest-range-i/
# Related Topics:
# Math

# Example:
# Input: A = [0,10], K = 2
# Output: 6


class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(0, max(A) - min(A) - 2*K)