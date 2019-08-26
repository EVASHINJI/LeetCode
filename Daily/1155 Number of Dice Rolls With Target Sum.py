# Url: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
# Related Topics:
# DP

# Example 1:
# Input: d = 1, f = 6, target = 3
# Output: 1
# Explanation: 
# You throw one die with 6 faces.  There is only one way to get a sum of 3.

# Example 2:
# Input: d = 2, f = 6, target = 7
# Output: 6
# Explanation: 
# You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
# 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target < d or target > d * f:
            return 0
        
        MOD = 10**9 + 7
        dp = [0] * (target + 1)
        for i in range(min(target, f)):
            dp[i+1] = 1
        for i in range(2, d + 1):
            new_dp = [0] * (target + 1)
            _sum = 0
            for j in range(i, min(target, i*f) + 1):
                _sum += dp[j - 1]
                if j - 1 >= f:
                    _sum -= dp[j - 1 - f]
                _sum = _sum % MOD
                new_dp[j] = _sum
            dp = new_dp
        return dp[target]
    