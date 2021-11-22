// Url: https://leetcode.com/problems/power-of-four/
// Related Topics:
// BitManipulation Math Recursion

// Example 1:
// Input: n = 16
// Output: true

// Example 2:
// Input: n = 5
// Output: false

// Creative 
// n & (n-1) can calculate the minium bit 1 of n. 
// mask=(10101010101010101010101010101010)2 & n == 0 means the 1-bit can only occur in the even bit.

class Solution {
    public boolean isPowerOfFour(int n) {
        return n > 0 && (n & (n - 1)) == 0 && (n & 0xaaaaaaaa) == 0;
    }
}