# Url: https://leetcode.com/problems/valid-mountain-array/
# Related Topics:
# Array 

# Example 1:
# Input: [2,1]
# Output: false

# Example 2:
# Input: [3,5,5]
# Output: false

# Example 3:
# Input: [0,3,2,1]
# Output: true


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        N = len(A)
        i = 0
        while i + 1 < N and A[i] < A[i+1]:
            i += 1
        if i == 0 or i == N - 1:
            return False
        while i + 1 < N and A[i] > A[i+1]:
            i += 1
        return i == N - 1