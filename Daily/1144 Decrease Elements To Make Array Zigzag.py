# Url: https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/
# Related Topics:
# Array

# Example 1:
# Input: nums = [1,2,3]
# Output: 2
# Explanation: We can decrease 2 to 0 or 3 to 1.

# Example 2:
# Input: nums = [9,6,1,6,2]
# Output: 4


class Solution:
    def movesToMakeZigzag(self, A: List[int]) -> int:
        A = [float('inf')] + A + [float('inf')]
        res = [0, 0]
        for i in range(1, len(A) - 1):
            res[i % 2] += max(0, A[i] - min(A[i - 1], A[i + 1]) + 1)
        return min(res)