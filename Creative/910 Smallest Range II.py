# Url: https://leetcode.com/problems/smallest-range-ii/
# Related Topics:
# Math Greedy

# Example:
# Input: A = [1,3,6], K = 3
# Output: 3
# Explanation: B = [4,6,3]

# Creative
# If cannot find the optimal boundary, can try every boundary


class Solution:
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        
        ans = A[-1] - A[0]
        ma, mi = A[-1] - K, A[0] + K
        for i in range(len(A) - 1):
            a, b = A[i], A[i+1]
            ans = min(ans, max(ma, a+K) - min(mi, b-K))
        return ans