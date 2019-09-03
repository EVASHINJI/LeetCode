# Url: https://leetcode.com/problems/maximum-width-ramp/
# Related Topics:
# Array

# Example 1:
# Input: [6,0,8,2,1,5]
# Output: 4
# Explanation: 
# The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.

# Example 2:
# Input: [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation: 
# The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.

# Creative
# Sorted by the val, return the origin idx of sorted arr


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        ans = 0
        mi = float('inf')
        for i in sorted(range(len(A)), key=A.__getitem__):
            ans = max(ans, i - mi)
            mi = min(mi, i)
        return ans
        