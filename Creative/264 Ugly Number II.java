// Url: https://leetcode.com/problems/ugly-number-ii/
// Related Topics:
// HashTable Math Heap PriorityQueue DP 

// Example 1:
// Input: n = 10
// Output: 12
// Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

// Example 2:
// Input: n = 1
// Output: 1
// Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

// Creative 
// use DP's idea, avoid duplicate num and sort time in heap opt

class Solution {
    public int nthUglyNumber(int n) {
        int[] dp = new int[n+1];
        int p2 = 1, p3 = 1, p5 = 1;
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            long next2 = dp[p2] * 2, next3 = dp[p3] * 3, next5 = dp[p5] * 5;
            long min = Math.min(Math.min(next2, next3), next5);
            dp[i] = (int) min;
            if (min == next2) p2++;
            if (min == next3) p3++;
            if (min == next5) p5++;
        }
        return dp[n];
    }
}