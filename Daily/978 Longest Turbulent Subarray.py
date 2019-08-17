# Url: https://leetcode.com/problems/longest-turbulent-subarray/
# Related Topics:
# Array DP SlidingWindow

# Example 1:
# Input: [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])

# Example 2:
# Input: [4,8,12,16]
# Output: 2


class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        prev = 0
        ans, c = 1, 1
        for i in range(1, len(A)):
            cur = A[i] - A[i-1]
            if prev*cur >= 0:
                ans = max(ans, c)
                c = 2 if cur != 0 else 0
            else:
                c += 1
            prev = cur
        ans = max(ans, c)
        return ans