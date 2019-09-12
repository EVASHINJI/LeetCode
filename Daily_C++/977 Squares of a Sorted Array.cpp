// Url: https://leetcode.com/problems/squares-of-a-sorted-array/
// Related Topics:
// Array TwoPointers

// Example 1:
// Input: [-4,-1,0,3,10]
// Output: [0,1,9,16,100]


class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        int i = 0, j = A.size() - 1;
        vector<int> ans;
        while (i <= j) {
            if (abs(A[i]) > abs(A[j])) {
                ans.push_back(pow(A[i++], 2));
            } else {
                ans.push_back(pow(A[j--], 2));
            }
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};