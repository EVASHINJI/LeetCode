// Url: https://leetcode.com/problems/get-maximum-in-generated-array/
// Related Topics:
// DP Array Simulation

// Example 1:
// Input: n = 7
// Output: 3
// Explanation: According to the given rules:
//   nums[0] = 0
//   nums[1] = 1
//   nums[(1 * 2) = 2] = nums[1] = 1
//   nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
//   nums[(2 * 2) = 4] = nums[2] = 1
//   nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
//   nums[(3 * 2) = 6] = nums[3] = 2
//   nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
// Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is 3.

// Example 2:
// Input: n = 2
// Output: 1
// Explanation: According to the given rules, the maximum between nums[0], nums[1], and nums[2] is 1.

class Solution {
    public int dp(int[] memo, int n) {
        if (memo[n] > 0) return memo[n];
        int i = n / 2;
        if ((n & 1) == 1) memo[n] = dp(memo, i) + dp(memo, i + 1);
        else memo[n] = dp(memo, i);
        return memo[n];
    }

    public int getMaximumGenerated(int n) {
        if (n < 2) return n;
        int[] memo = new int[n + 1];
        memo[0] = 0;
        memo[1] = 1;
        int max = 0;
        for (int i = n; i > n/2; i--) {
            int x = dp(memo, i);
            if (x > max) max = x;
        }
        return max;
    }
}