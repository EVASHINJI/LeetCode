// Url: https://leetcode.com/problems/minimum-absolute-difference/
// Related Topics:
// Array

// Example 1:
// Input: arr = [4,2,1,3]
// Output: [[1,2],[2,3],[3,4]]
// Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

// Example 2:
// Input: arr = [1,3,6,10,15]
// Output: [[1,3]]

// Example 3:
// Input: arr = [3,8,-10,23,19,-4,-14,27]
// Output: [[-14,-10],[19,23],[23,27]]

class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        List<List<Integer>> ans = new ArrayList<>();
        Arrays.sort(arr);
        int min = Integer.MAX_VALUE;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] - arr[i-1] < min) {
                min = arr[i] - arr[i-1];
            }
        }
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] - arr[i-1] == min) {
                ans.add(Arrays.asList(arr[i-1], arr[i]));
            }
        }
        return ans;
    }
}