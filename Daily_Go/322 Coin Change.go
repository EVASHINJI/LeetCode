// Url: https://leetcode.com/problems/coin-change/
// Related Topics:
// Array DP BreadthFirstSearch

// Example 1:
// Input: coins = [1,2,5], amount = 11
// Output: 3
// Explanation: 11 = 5 + 5 + 1

// Example 2:
// Input: coins = [2], amount = 3
// Output: -1

func coinChange(coins []int, amount int) int {
    if amount == 0 {
        return 0
    }
    dp := make([]int, amount + 1)
    for i := 1; i <= amount; i++ {
        dp[i] = -1
    }
    for _, coin := range coins {
        for i:= coin; i <= amount; i++ {
            if dp[i - coin] >= 0 {
                if dp[i] == -1 || dp[i-coin] + 1 < dp[i] {
                    dp[i] = dp[i-coin] + 1 
                }
            }
        }
    }
    return dp[amount]
}