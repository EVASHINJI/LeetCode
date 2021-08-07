// Url: https://leetcode.com/problems/mean-of-array-after-removing-some-elements/
// Related Topics:
// Array Sorting

// Example 1:
// Input: arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
// Output: 2.00000
// Explanation: After erasing the minimum and the maximum values of this array, all elements are equal to 2, so the mean is 2.

// Example 2:
// Input: arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
// Output: 4.00000

// Example 3:
// Input: arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
// Output: 4.77778

// Creative 
// use findKthLargest idea to calculate sum in range 

class Solution {
    public int findKth(int[] nums, int l, int r, int k) {
        if (l >= r) return k;
        int pivot = nums[l];
        int i = l, j = r;
        while (i < j) {
            while (i < j && nums[j] >= pivot) j--;
            if (i < j) nums[i++] = nums[j];
            while (i < j && nums[i] <= pivot) i++;
            if (i < j) nums[j--] = nums[i];
        }
        nums[i] = pivot;
        if (i > k) return findKth(nums, l, i - 1, k);
        if (i < k) return findKth(nums, i + 1, r, k);
        return k;
    }

    public double trimMean(int[] arr) {
        int trim = arr.length / 20;
        int out = 0;
        findKth(arr, 0, arr.length - 1, trim);
        for (int i = 0; i < trim; i++) out += arr[i];
        findKth(arr, 0, arr.length - 1, arr.length - trim);
        int sum = 0;
        for (int i = 0; i < arr.length - trim; i++) {
            sum += arr[i];
        }
        return 1.0 * (sum - out) / (arr.length - 2*trim);
    }
}