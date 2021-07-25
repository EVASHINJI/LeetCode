// Url: https://leetcode.com/problems/next-greater-element-i/
// Related Topics:
// Array HashTable Stack MonotonicStack

// Example 1:
// Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
// Output: [-1,3,-1]
// Explanation: The next greater element for each value of nums1 is as follows:
// - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
// - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
// - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

// Example 2:
// Input: nums1 = [2,4], nums2 = [1,2,3,4]
// Output: [3,-1]
// Explanation: The next greater element for each value of nums1 is as follows:
// - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
// - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Stack<Integer> st = new Stack<>();
        int l1 = nums1.length;
        int l2 = nums2.length;
        Map<Integer, Integer> hm = new HashMap<>();
        for (int i = l2 - 1; i >= 0; i--) {
            while (!st.empty()) {
                if (nums2[i] < st.peek()) {
                    hm.put(nums2[i], st.peek());
                    st.push(nums2[i]);
                    break;
                }
                st.pop();
            }
            if (st.empty()) {
                hm.put(nums2[i], -1);
                st.push(nums2[i]);
            }
        }
        int[] ans = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            ans[i] = hm.get(nums1[i]);
        }
        return ans;
    }
}