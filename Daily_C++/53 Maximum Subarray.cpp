// Url: https://leetcode.com/problems/maximum-subarray/
// Related Topics:
// DP Array DivideAndConquer

// Example:
// Input: [-2,1,-3,4,-1,2,1,-5,4],
// Output: 6
// Explanation: [4,-1,2,1] has the largest sum = 6.


class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (!nums.size()) return 0;
        int ans = nums[0], cur_sum = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            if (cur_sum < 0) cur_sum = 0;
            cur_sum += nums[i];
            ans = max(ans, cur_sum);
        }
        return ans;
    }
};