// Url: https://leetcode.com/problems/hamming-distance/
// Related Topics:
// BitManipulation

// Example 1:
// Input: x = 1, y = 4
// Output: 2
// Explanation:
// 1   (0 0 0 1)
// 4   (0 1 0 0)
//        ↑   ↑
// The above arrows point to positions where the corresponding bits are different.

// Example 2:
// Input: x = 3, y = 1
// Output: 1

class Solution {
    public int hammingDistance(int x, int y) {
        int ans = 0;
        int ham = x ^ y;
        while (ham != 0) {
            ham &= ham - 1;
            ans++;
        }
        return ans;
    }
}