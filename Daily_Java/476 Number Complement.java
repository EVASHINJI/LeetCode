// Url: https://leetcode.com/problems/number-complement/
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
    public int findComplement(int num) {
        long a = 1;
        while (num >= a) {
            a <<= 1;
        }
        return (int)(a - num - 1);
    }
}