# Url: https://leetcode.com/problems/uncrossed-lines/
# Related Topics:
# Array

# Example 1:
# Input: A = [1,4,2], B = [1,2,4]
# Output: 2
# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        l_a, l_b = len(A), len(B)
        dp = [0] * (l_b + 1)
        for a in A:
            temp_dp = [0] * (l_b + 1)
            for j, b in enumerate(B):
                if a == b:
                    temp_dp[j] = dp[j-1] + 1
                else:
                    temp_dp[j] = max(dp[j], temp_dp[j-1])
            dp = temp_dp
        return max(dp)