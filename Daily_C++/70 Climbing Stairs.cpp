// Url: https://leetcode.com/problems/climbing-stairs/
// Related Topics:
// DP

// Example 1:
// Input: 2
// Output: 2
// Explanation: There are two ways to climb to the top.
// 1. 1 step + 1 step
// 2. 2 steps

// Example 2:
// Input: 3
// Output: 3
// Explanation: There are three ways to climb to the top.
// 1. 1 step + 1 step + 1 step
// 2. 1 step + 2 steps
// 3. 2 steps + 1 step


class Solution {
public:
    int climbStairs(int n) {
        if (n <= 3) return n;
        int step1 = 1, step2 = 2;
        for (int i = 3; i < n; i++) {
            int temp = step1 + step2;
            step1 = step2;
            step2 = temp;
        }
        return step1 + step2;
    }
};