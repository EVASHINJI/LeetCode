// Url: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
// Related Topics:
// Array

// Example 1:
// Input: arr = [1,2,2,6,6,6,6,7,10]
// Output: 6

// Example 2:
// Input: arr = [1,1]
// Output: 1

class Solution {
    public int findSpecialInteger(int[] arr) {
        int quarter = arr.length / 4;
        int i = 0;
        while (i < arr.length) {
            if (arr[i + quarter] == arr[i]) return arr[i];
            i++;
        }
        return -1;
    }
}