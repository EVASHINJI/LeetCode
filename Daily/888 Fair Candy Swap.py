# Url: https://leetcode.com/problems/fair-candy-swap/
# Related Topics:
# Array

# Example 1:
# Input: A = [1,1], B = [2,2]
# Output: [1,2]

# Example 2:
# Input: A = [1,2], B = [2,3]
# Output: [1,2]


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_A, sum_B = sum(A), sum(B)
        delta = int((sum_A + sum_B) / 2 - sum_A)
        set_B = set(B)
        for a in A:
            b = a + delta
            if b in set_B:
                return [a, b]