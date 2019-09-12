// Url: https://leetcode.com/problems/sort-array-by-parity/
// Related Topics:
// Array

// Example 1:
// Input: [3,1,2,4]
// Output: [2,4,3,1]
// The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        int i, j;
        i = 0;
        j = A.size() - 1;
        while (i < j) {
            while (i < A.size() && A[i] % 2 == 0) i++;
            while (j >=0 && A[j] % 2 == 1) j--;
            if (i < j) {
                int tmp = A[i];
                A[i] = A[j];
                A[j] = tmp;
            }
        }
        return A;
    }
};