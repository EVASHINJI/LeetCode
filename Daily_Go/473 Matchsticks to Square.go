// Url: https://leetcode.com/problems/matchsticks-to-square/
// Related Topics:
// Array DP Backtracking BitManipulation BitMask

// Example 1:
// Input: matchsticks = [1,1,2,2,2]
// Output: true
// Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

// Example 2:
// Input: matchsticks = [3,3,3,3,4]
// Output: false
// Explanation: You cannot find a way to form a square with all the matchsticks.

func makesquare(matchsticks []int) bool {
    sum := 0
    for _, m := range matchsticks {
        sum += m
    }
    if sum == 0 || sum % 4 > 0 {
        return false
    }
    target := sum / 4
    used := make([]bool, len(matchsticks))
    var dfs func(int, int, int) bool
    dfs = func(curSum int, idx int, group int) bool {
        if curSum == target {
            group += 1
            curSum = 0
        }
        if group == 3 {
            return true
        }
        if curSum == 0 {
            i := 0
            for i < len(matchsticks) && used[i] {
                i++;
            }
            if i == len(matchsticks) {
                return false
            }
            used[i] = true
            curSum = matchsticks[i]
            if dfs(curSum, i+1, group) {
                return true
            }
            used[i] = false
        } else {
            for i := idx; i < len(matchsticks); i++ {
                if used[i] || matchsticks[i] + curSum > target {
                    continue
                }
                used[i] = true
                if dfs(curSum + matchsticks[i], i+1, group) {
                    return true
                }
                used[i] = false
            }
        }
        return false
    }
    return dfs(0, 0, 0)
}