// Url: https://leetcode.com/problems/next-greater-element-ii/
// Related Topics:
// Array Stack MonotonicStack

// Example 1:
// Input: nums = [1,2,1]
// Output: [2,-1,2]
// Explanation: The first 1's next greater number is 2; 
// The number 2 can't find next greater number. 
// The second 1's next greater number needs to search circularly, which is also 2.

// Example 2:
// Input: nums = [1,2,3,4,3]
// Output: [2,3,4,-1,4]

class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] nextGreater = new int[nums.length];
        Stack<Integer> posStack = new Stack<>();

        // 构造单调栈
        for (int i = n - 1; i >= 0; i--) {
            if (posStack.isEmpty()) {
                posStack.push(i);
            } else if (nums[i] >= nums[posStack.peek()]) {
                posStack.pop();
                posStack.push(i);
            } else {
                posStack.push(i);
            }
        }

        for (int i = n - 1; i >= 0; i--) {
            while (!posStack.isEmpty() && nums[i] >= nums[posStack.peek()]) {
                posStack.pop();
            }
            if (posStack.isEmpty()) nextGreater[i] = -1;
            else nextGreater[i] = nums[posStack.peek()];
            posStack.push(i);
        }
        return nextGreater;
    }
}