// Url: https://leetcode.com/problems/move-zeroes/
// Related Topics:
// Array TwoPointers

// Example:
// Input: [0,1,0,3,12]
// Output: [1,3,12,0,0]


class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0;
        for (int last=0, cur = 0; cur < nums.size(); cur++) {
            if (nums[cur]) std::swap(nums[last++], nums[cur]);
        }
    }
};