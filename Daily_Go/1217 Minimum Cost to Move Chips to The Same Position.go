// Url: https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
// Related Topics:
// Array Math Greedy

// Example 1:
// Input: position = [1,2,3]
// Output: 1
// Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
// Second step: Move the chip at position 2 to position 1 with cost = 1.
// Total cost is 1.

func minCostToMoveChips(position []int) int {
    odd, even := 0, 0
    for _, pos := range position {
        if pos % 2 == 0 {
            even++
        } else {
            odd++
        }
    }
    if odd < even {
        return odd
    }
    return even
}