# Url: https://leetcode.com/problems/sort-array-by-parity-ii/
# Related Topics:
# Array Sort

# Example 1:
# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        o = 1
        for e in range(0, len(A), 2):
            if A[e] % 2:
                while A[o] % 2:
                    o += 2
                A[e], A[o] = A[o], A[e]
        return A