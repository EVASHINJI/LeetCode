// Url: https://leetcode.com/problems/coin-change-2/
// Related Topics:
// Array DP

// Example 1:
// Input: amount = 5, coins = [1,2,5]
// Output: 4
// Explanation: there are four ways to make up the amount:
// 5=5
// 5=2+2+1
// 5=2+1+1+1
// 5=1+1+1+1+1

// Example 2:
// Input: amount = 3, coins = [2]
// Output: 0
// Explanation: the amount of 3 cannot be made up just with coins of 2.

// Example 3:
// Input: amount = 10, coins = [10]
// Output: 1

func change(amount int, coins []int) int {
    if amount == 0 {
        return 1
    }
    dp := make([]int, amount + 1)
    dp[0] = 1
    for _, coin := range coins {
        for i := coin; i <= amount; i++ {
            dp[i] += dp[i - coin]
        }
    }
    return dp[amount]
}