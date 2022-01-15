// Url: https://leetcode.com/problems/complement-of-base-10-integer/
// Related Topics:
// BitManipulation

// Example 1:
// Input: num = 5
// Output: 2
// Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

// Example 2:
// Input: num = 1
// Output: 0
// Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

class Solution {
    public int bitwiseComplement(int n) {
        return ((1 << Integer.toBinaryString(n).length()) - 1) ^ n;
    }
}