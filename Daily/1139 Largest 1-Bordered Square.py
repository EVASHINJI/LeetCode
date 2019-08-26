# Url: https://leetcode.com/problems/largest-1-bordered-square/
# Related Topics:
# DP

# Example 1:
# Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
# Output: 9

# Example 2:
# Input: grid = [[1,1,0,0]]
# Output: 1


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        R, C = len(grid), len(grid[0])
        right = [[0] * C for _ in range(R)]
        down = [[0] * C for _ in range(R)]
        
        for i in range(R-1, -1, -1):
            for j in range(C-1, -1, -1):
                right_prev = 0 if j == C-1 else right[i][j+1]
                down_prev = 0 if i == R-1 else down[i+1][j]
                if grid[i][j]:
                    right[i][j] = right_prev + 1
                    down[i][j] = down_prev + 1
        
        ans = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j]:
                    l = min(right[i][j], down[i][j])
                    for k in range(l-1, -1, -1):
                        if k < ans or i + k >= R or j + k >= C:
                            continue
                        if down[i][j+k] > k and right[i+k][j] > k:
                            ans = k + 1
        return ans*ans