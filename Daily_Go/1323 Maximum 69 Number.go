// Url: https://leetcode.com/problems/maximum-69-number/
// Related Topics:
// Math Greedy

// Example 1:
// Input: num = 9669
// Output: 9969
// Explanation: 
// Changing the first digit results in 6669.
// Changing the second digit results in 9969.
// Changing the third digit results in 9699.
// Changing the fourth digit results in 9666. 
// The maximum number is 9969.

// Example 2:
// Input: num = 9996
// Output: 9999
// Explanation: Changing the last digit 6 to 9 results in the maximum number.

func maximum69Number (num int) int {
    n := num
    highPos, curPos := -1, 0
    for n > 0 {
        i := n % 10
        if (i == 6) {
            highPos = curPos
        }
        n /= 10
        curPos++
    }
    if (highPos >= 0) {
        num += 3 * int(math.Pow10(highPos))
    }
    return num
}