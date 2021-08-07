// Url: https://leetcode.com/problems/decompress-run-length-encoded-list/
// Related Topics:
// Array

// Example 1:
// Input: nums = [1,2,3,4]
// Output: [2,4,4,4]
// Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
// The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
// At the end the concatenation [2] + [4,4,4] is [2,4,4,4].

// Example 2:
// Input: nums = [1,1,2,3]
// Output: [1,3,3]

class Solution {
    public int[] decompressRLElist(int[] nums) {
        List<Integer> ans = new ArrayList<Integer>();
        for (int i = 0; i < nums.length; i += 2) {
            for (int j = 0; j < nums[i]; j++) {
                ans.add(nums[i+1]);
            }
        }
        int[] result = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) {
            result[i]= ans.get(i);
        }
        return result;
    }
}