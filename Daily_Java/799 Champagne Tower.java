// Url: https://leetcode.com/problems/champagne-tower/
// Related Topics:
// DP

// Example 1:
// Input: poured = 1, query_row = 1, query_glass = 1
// Output: 0.00000
// Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.

class Solution {
    public double champagneTower(int poured, int queryRow, int queryGlass) {
        double[][] dp = new double[queryRow + 1][queryRow + 1];
        dp[0][0] = poured;
        for (int i = 0; i < queryRow; i++) {
            for (int j = 0; j <= i; j++) {
                double flow = (dp[i][j] - 1) / 2;
                if (flow > 0) {
                    dp[i+1][j] += flow;
                    dp[i+1][j+1] += flow;
                }
            }
        }
        return Math.min(1,dp[queryRow][queryGlass]);
    }
}