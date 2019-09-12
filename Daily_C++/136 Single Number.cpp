// Url: https://leetcode.com/problems/single-number/
// Related Topics:
// HashTable BitManipulation

// Example 1:
// Input: [2,2,1]
// Output: 1


class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (auto &n: nums) {
            ans ^= n;
        }
        return ans;
    }
};