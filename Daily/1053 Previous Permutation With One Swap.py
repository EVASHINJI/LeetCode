# Url: https://leetcode.com/problems/previous-permutation-with-one-swap/
# Related Topics:
# Array Greedy

# Example 1:
# Input: [3,2,1]
# Output: [3,1,2]
# Explanation: Swapping 2 and 1.

# Example 2:
# Input: [1,1,5]
# Output: [1,1,5]
# Explanation: This is already the smallest permutation.


class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        N = len(A)
        for i in range(N-1, 0, -1):
            if A[i-1] > A[i]:
                max_j = i
                for j in range(i, N):
                    if A[j] < A[i-1] and A[j] > A[max_j]:
                        max_j = j
                A[i-1], A[max_j] = A[max_j], A[i-1]
                break
        return A