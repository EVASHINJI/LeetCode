# Url: https://leetcode.com/problems/last-stone-weight-ii/
# Related Topics:
# DP

# Example:
# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
# we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
# we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we can combine 1 and 1 to get 0 so the array converts to [1] then that's the optimal value.

# Creative
# Convert problem to 0-1Pack


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        W = sum(stones) // 2
        dp = [float('-inf')] * (W+1)
        dp[0] = 0
        sum_s = 0
        for s in stones:
            sum_s += s
            for i in range(min(W,sum_s), s - 1, -1):
                dp[i] = max(dp[i], dp[i-s] + 1)
        for i in range(W, -1, -1):
            if dp[i] > 0:
                return sum_s - i - i
        return 0