// Url: https://leetcode.com/problems/majority-element/
// Related Topics:
// Array DivideAndConquer BitManipulation

// Example 1:
// Input: [3,2,3]
// Output: 3
// Example 2:
// Input: [2,2,1,1,1,2,2]
// Output: 2


class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int vote = nums[0];
        int cnt = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (cnt == 0) {
                vote = nums[i];
                cnt = 1;
            } else if (vote == nums[i]) cnt++;
            else cnt--;
        }
        return vote;
    }
};