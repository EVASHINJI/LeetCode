# Url: https://leetcode.com/problems/domino-and-tromino-tiling/
# Related Topics:
# DP

# Example:
# Input: 3
# Output: 5
# Explanation: 
# The five different ways are listed below, different letters indicates different tiles:
# XYZ XXZ XYY XXY XYY
# XYZ YYZ XZZ XYY XXY


class Solution:
    def numTilings(self, N: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * max(N+1, 4)
        dp[1] = 1
        dp[2] = 2
        _sum = 2
        for i in range(3, N+1):
            dp[i] = (dp[i-1] + dp[i-2] + _sum) % MOD
            _sum += dp[i-2] * 2
            _sum %= MOD
        return dp[N]