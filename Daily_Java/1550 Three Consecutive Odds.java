// Url: https://leetcode.com/problems/three-consecutive-odds/
// Related Topics:
// Array

// Example 1:
// Input: arr = [2,6,4,1]
// Output: false
// Explanation: There are no three consecutive odds.

// Example 2:
// Input: arr = [1,2,34,3,4,5,7,23,12]
// Output: true
// Explanation: [5,7,23] are three consecutive odds.

class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        int flag = 0;
        for (int i : arr) {
            if (i % 2 == 0) {
                flag = 0;
            } else {
                flag += 1;
                if (flag >= 3) return true;
            }
        }
        return false;
    }
}