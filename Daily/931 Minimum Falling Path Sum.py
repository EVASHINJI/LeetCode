# Url: https://leetcode.com/problems/minimum-falling-path-sum/
# Related Topics:
# DP

# Example 1:
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: 12
# Explanation: 
# The possible falling paths are:
# [1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
# [2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
# [3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
# The falling path with the smallest sum is [1,4,7], so the answer is 12.


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        N = len(A)
        while len(A) >= 2:
            row = A.pop()
            for i in range(N):
                A[-1][i] += min(row[max(0, i-1): min(N,i+2)])
        return min(A[0])