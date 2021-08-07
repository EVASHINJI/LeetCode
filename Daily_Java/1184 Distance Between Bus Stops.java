// Url: https://leetcode.com/problems/distance-between-bus-stops/
// Related Topics:
// Array

// Example 1:
// Input: distance = [1,2,3,4], start = 0, destination = 1
// Output: 1
// Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.

// Example 2:
// Input: distance = [1,2,3,4], start = 0, destination = 2
// Output: 3
// Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.

// Example 3:
// Input: distance = [1,2,3,4], start = 0, destination = 3
// Output: 4
// Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.

class Solution {
    public int distanceBetweenBusStops(int[] distance, int start, int destination) {
        int[] disSum = new int[distance.length + 1];
        for (int i = 0; i < distance.length; i++) {
            disSum[i + 1] = disSum[i] + distance[i];
        }
        int total = disSum[distance.length];
        int dis = start < destination ? disSum[destination] - disSum[start]: disSum[start] - disSum[destination];
        return Math.min(dis, total - dis);
    }
}