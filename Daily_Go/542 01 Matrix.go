// Url: https://leetcode.com/problems/01-matrix/
// Related Topics:
// Array DP BreadthFirstSearch Matrix

// Example 1:
// Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
// Output: [[0,0,0],[0,1,0],[0,0,0]]

// Example 2:
// Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
// Output: [[0,0,0],[0,1,0],[1,2,1]]

func min(a int, b int) int {
    if a < b {
        return a
    } else {
        return b
    }
}

func updateMatrix(mat [][]int) [][]int {
    m, n := len(mat), len(mat[0])
    dp := make([][]int, m)
    max := 1000000000
    for i := 0; i < m; i++ {
        dp[i] = make([]int, n)
        for j := 0; j < n; j++ {
            dp[i][j] = max
            if mat[i][j] == 0 {
                dp[i][j] = 0
                continue
            }
            if i > 0 {
                dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
            }
            if j > 0 {
                dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
            }
        }
    }
    for i := m-1; i>=0; i-- {
        for j := n-1; j>=0; j-- {
            if dp[i][j] == 0 {
                continue
            }
            if i < m - 1 {
                dp[i][j] = min(dp[i][j],dp[i+1][j]+1)
            }
            if j < n - 1 {
                dp[i][j] = min(dp[i][j], dp[i][j+1]+1)
            }
        }
    }
    return dp
}