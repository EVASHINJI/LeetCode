// Url: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
// Related Topics:
// Array

// Example:
// Input:
// [4,3,2,7,8,2,3,1]
// Output:
// [5,6]

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> ans;
        for (auto &n: nums) {
            int idx = abs(n) - 1;
            if (nums[idx] > 0) nums[idx] = -nums[idx];
        }
        for (int i = 0; i < nums.size(); i++) 
            if (nums[i] > 0) ans.push_back(i+1);
        return ans;
    }
};