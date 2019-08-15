# Url: https://leetcode.com/problems/monotonic-array/
# Related Topics:
# Array

# Example 1:
# Input: [1,2,2,3]
# Output: true

# Example 2:
# Input: [6,5,4,4]
# Output: true


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        delta = A[0] - A[-1]
        for a, b in zip(A, A[1:]):
            if (a - b) * delta < 0:
                return False
            if a - b != 0:
                delta = a - b
        return True
        