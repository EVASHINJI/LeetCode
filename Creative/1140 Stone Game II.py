# Url: https://leetcode.com/problems/stone-game-ii/
# Related Topics:
# DP

# Example 1:
# Input: piles = [2,7,9,4,4]
# Output: 10
# Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex takes two piles at the beginning, then Lee can take all three piles left. In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        dp = [[0]*N for _ in range(N)]
        def sgii(A, i, m):
            if i + 2*m >= N:
                return A[i]
            if not dp[i][m]:
                dp[i][m] = A[i] - min([sgii(A, i+x, max(m, x)) for x in range(1, 2*m+1)])
            return dp[i][m]
        
        A = piles[:]
        for i in range(N-2, -1, -1):
            A[i] += A[i+1]
        sgii(A, 0, 1)
        return dp[0][1]