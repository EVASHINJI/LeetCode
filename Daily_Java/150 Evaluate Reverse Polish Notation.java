// Url: https://leetcode.com/problems/evaluate-reverse-polish-notation/
// Related Topics:
// Array Stack Math

// Example 1:
// Input: tokens = ["2","1","+","3","*"]
// Output: 9
// Explanation: ((2 + 1) * 3) = 9

// Example 2:
// Input: tokens = ["4","13","5","/","+"]
// Output: 6
// Explanation: (4 + (13 / 5)) = 6

class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int[] earn = new int[gas.length];
        int sum = 0;
        int circleSum = 0;
        int startPos = 0;
        for (int i = 0; i < gas.length; i++) {
            earn[i] = gas[i] - cost[i];
            circleSum += earn[i];
            sum += earn[i];
            if (sum < 0) {
                sum = 0;
                startPos = i + 1;
            }
        }
        if (circleSum < 0) return -1;
        return startPos;
    }
}