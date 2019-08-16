# Url: https://leetcode.com/problems/best-sightseeing-pair/
# Related Topics:
# Array

# Example 1:
# Input: [8,1,5,2,6]
# Output: 11
# Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        cur, ans = 0, 0
        for a in A:
            ans = max(ans, cur+a)
            cur = max(a, cur) - 1
        return ans