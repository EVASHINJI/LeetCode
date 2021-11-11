// Url: https://leetcode.com/problems/split-a-string-in-balanced-strings/
// Related Topics:
// String Greedy Counting

// Example 1:
// Input: s = "RLRRLLRLRL"
// Output: 4
// Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

// Example 2:
// Input: s = "RLLLLRRRLR"
// Output: 3
// Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

// Example 3:
// Input: s = "LLLLRRRR"
// Output: 1
// Explanation: s can be split into "LLLLRRRR".

func balancedStringSplit(s string) int {
    cnt := 0
    balance := 0
    for _, c := range s {
        if c == 'L' {
            balance++
        } else {
            balance--
        }
        if balance == 0 {
            cnt++
        }
    }
    return cnt
}