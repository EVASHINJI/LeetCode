// Url: https://leetcode.com/problems/largest-perimeter-triangle/
// Related Topics:
// Array Math Sorting Greedy

// Example 1:
// Input: nums = [2,1,2]
// Output: 5

// Example 2:
// Input: nums = [1,2,1]
// Output: 0

// Example 3:
// Input: nums = [3,2,3,4]
// Output: 10

// Example 4:
// Input: nums = [3,6,2,3]
// Output: 8

class Solution {
    public int largestPerimeter(int[] nums) {
         Arrays.sort(nums);
         for (int i = nums.length - 3; i >= 0; i--) {
             if (nums[i] + nums[i+1] > nums[i + 2]) return nums[i] + nums[i+1] + nums[i+2];
         }
         return 0;
    }
}