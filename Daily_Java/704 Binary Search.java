// Url: https://leetcode.com/problems/binary-search/
// Related Topics:
// Array BinarySearch
// Tips: 二分查找时最好还是不要l和r都+1 -1，最后停下的位置可能并不是想要的

// Example 1:
// Input: nums = [-1,0,3,5,9,12], target = 9
// Output: 4
// Explanation: 9 exists in nums and its index is 4

// Example 2:
// Input: nums = [-1,0,3,5,9,12], target = 2
// Output: -1
// Explanation: 2 does not exist in nums so return -1

class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length;
        while (l < r) {
            int mid = (l + r) / 2;
            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) l = mid + 1;
            else r = mid;
        }
        return -1;
    }
}