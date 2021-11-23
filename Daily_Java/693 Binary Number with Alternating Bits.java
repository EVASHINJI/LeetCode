// Url: https://leetcode.com/problems/binary-number-with-alternating-bits/
// Related Topics:
// BitManipulation

// Example 1:
// Input: n = 5
// Output: true
// Explanation: The binary representation of 5 is: 101

// Example 2:
// Input: n = 7
// Output: false
// Explanation: The binary representation of 7 is: 111.

class Solution {
    public boolean hasAlternatingBits(int n) {
        int lastBit = n & 1;
        n >>= 1;
        while (n != 0) {
            if ((n & 1) == lastBit) return false;
            lastBit = n & 1;
            n >>= 1;
        }
        return true;
    }
}