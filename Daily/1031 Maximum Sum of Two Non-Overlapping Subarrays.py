# Url: https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/
# Related Topics:
# Array 

# Example 1:
# Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
# Output: 20
# Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.

# Example 2:
# Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
# Output: 29
# Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        sum_A = [0]
        for a in A:
            sum_A.append(sum_A[-1] + a)
        res, l_max, m_max = sum_A[L+M], sum_A[L], sum_A[M]
        for i in range(L+M, len(sum_A)):
            l_max = max(l_max, sum_A[i-M] - sum_A[i-M-L])
            m_max = max(m_max, sum_A[i-L] - sum_A[i-M-L])
            res = max(res, l_max + sum_A[i] - sum_A[i-M], m_max + sum_A[i] - sum_A[i-L])
        return res