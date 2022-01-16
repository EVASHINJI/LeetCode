// Url: https://leetcode.com/problems/longest-mountain-in-array/
// Related Topics:
// Array DP TwoPointers Enumeration

// Example 1:
// Input: arr = [2,1,4,7,3,2,5]
// Output: 5
// Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

class Solution {
    public int longestMountain(int[] arr) {
        if (arr.length < 3) return 0;
        int maxLength = 0;
        for (int i = 0; i < arr.length - 2; i++) {
            if (arr[i] < arr[i+1] && arr[i+1] > arr[i+2]) {
                int left = i;
                int right = i+2;
                while (left > 0 && arr[left-1] < arr[left]) left--;
                while (right < arr.length - 1 && arr[right] > arr[right + 1]) right++;
                maxLength = Math.max(maxLength, right - left + 1);
                i = right - 1; // because at the end of "for" loop i will +1
            }
        }
        return maxLength;
    }
}