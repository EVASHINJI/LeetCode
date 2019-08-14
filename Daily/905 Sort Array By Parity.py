# Url: https://leetcode.com/problems/sort-array-by-parity/
# Related Topics:
# Array

# Example 1:
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while i < j:
            while i < len(A) and A[i] % 2 == 0:
                i += 1
            while j >= 0 and A[j] % 2 == 1:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
        return A
        