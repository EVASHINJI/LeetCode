# Url: https://leetcode.com/problems/can-i-win/
# Related Topics:
# DP MiniMax

# Example:
# Input:
# maxChoosableInteger = 10
# desiredTotal = 11
# Output:
# false
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
# Same with other integers chosen by the first player, the second player will always win.

# Creative
# DFS with BackTracking


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (maxChoosableInteger+1)*maxChoosableInteger/2 < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True
        
        use = ['0'] * (maxChoosableInteger+1)
        dp = {}
        def helper(d):
            if d <= 0:
                return False
            key = ''.join(use)
            if key not in dp:
                for i in range(1, maxChoosableInteger + 1):
                    if use[i] == '0':
                        use[i] = '1'
                        if not helper(d-i):
                            dp[key] = True
                            use[i] = '0'
                            return True
                        use[i] = '0'
                dp[key] = False
            return dp[key]
        
        return helper(desiredTotal)