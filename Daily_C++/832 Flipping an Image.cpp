// Url: https://leetcode.com/problems/flipping-an-image/
// Related Topics:
// Array

// Example 1:
// Input: [[1,1,0],[1,0,1],[0,0,0]]
// Output: [[1,0,0],[0,1,0],[1,1,1]]
// Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
// Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        for (auto & row: A) reverse(row.begin(), row.end());
        for (auto & row: A) for (auto & elem: row) elem ^= 1;
        return A;
    }
};