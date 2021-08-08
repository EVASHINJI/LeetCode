// Url: https://leetcode.com/problems/n-th-tribonacci-number/
// Related Topics:
// DP Math Memoization

// Example 1:
// Input: n = 4
// Output: 4
// Explanation:
// T_3 = 0 + 1 + 1 = 2
// T_4 = 1 + 1 + 2 = 4

// Example 2:
// Input: n = 25
// Output: 1389537

class Solution {
    public int tribonacci(int n) {
        int[] dp = new int[]{0, 1, 1};
        if (n < 3) return dp[n];
        int ans = dp[2];
        while (n >= 3) {
            ans = dp[2] + dp[1] + dp[0];
            dp[0] = dp[1];
            dp[1] = dp[2];
            dp[2] = ans;
            n--;
        }
        return ans;
    }
}