// Url: https://leetcode.com/problems/kth-largest-element-in-an-array/
// Related Topics:
// Array DivideAndConquer Sorting Heap QuickSelect

// Example 1:
// Input: nums = [3,2,1,5,6,4], k = 2
// Output: 5

// Example 2:
// Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
// Output: 4

// Creative 
// use partition idea in QuickSort 

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

    public int findKthLargest(int[] nums, int k) {
        return nums[findKth(nums, 0, nums.length - 1, nums.length - k)];
    }
}