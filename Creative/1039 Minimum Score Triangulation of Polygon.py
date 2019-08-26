# Url: https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
# Related Topics:
# DP

# Example 1:
# Input: [1,3,1,4,1,5]
# Output: 13
# Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.


class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        N = len(A)
        dp = [[0]* N for _ in range(N)]
        for d in range(2, N):
            for i in range(N - d):
                j = i + d
                dp[i][j] = min(dp[i][k] + dp[k][j] + A[i]*A[k]*A[j] for k in range(i + 1, j))
        return dp[0][-1]
            