# Url: https://leetcode.com/problems/knight-dialer/
# Related Topics:
# DP

# Example 1:
# Input: 1
# Output: 10
# Example 2:
# Input: 2
# Output: 20


class Solution:
    def knightDialer(self, N: int) -> int:
        nxt = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        MOD = 10**9+7
        dp = [1] * 10
        for _ in range(N-1):
            new_dp = [0] * 10
            for i in range(10):
                for k in nxt[i]:
                    new_dp[i] = (new_dp[i] + dp[k]) % MOD
            dp = new_dp
        return sum(dp) % MOD