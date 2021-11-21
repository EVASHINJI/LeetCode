// Url: https://leetcode.com/problems/reverse-bits/
// Related Topics:
// DivideAndConquer BitManipulation

// Example 1:
// Input: n = 00000010100101000001111010011100
// Output:    964176192 (00111001011110000010100101000000)
// Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

// Example 2:
// Input: n = 11111111111111111111111111111101
// Output:   3221225471 (10111111111111111111111111111111)
// Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.

// Creative 
// Divide and Conquer

public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int rev = 0;
        for (int i = 0; i < 32 && n != 0; i++) {
            rev |= (n & 1) << (31 - i);
            n = n >>> 1;
        }
        return rev;
    }
}

public class Solution {
    private static final int M1 = 0x55555555; // 01010101010101010101010101010101
    private static final int M2 = 0x33333333; // 00110011001100110011001100110011
    private static final int M4 = 0x0f0f0f0f; // 00001111000011110000111100001111
    private static final int M8 = 0x00ff00ff; // 00000000111111110000000011111111

    public int reverseBits(int n) {
        n = (n & M8) << 8 | (n >>> 8) & M8;
        n = (n & M4) << 4 | (n >>> 4) & M4;
        n = (n & M2) << 2 | (n >>> 2) & M2;
        n = (n & M1) << 1 | (n >>> 1) & M1;
        return n << 16 | n >>> 16;
    }
}

