# Url: https://leetcode.com/problems/sum-of-subarray-minimums/
# Related Topics:
# Array Stack

# Example 1:
# Input: [3,1,2,4]
# Output: 17
# Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        N = len(A)
        MOD = 10**9 + 7
        prv, nxt = [0] * N, [0] * N
        stack = []
        for i in range(N):
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()
            prv[i] = stack[-1] if stack else -1
            stack.append(i)
        stack = []
        
        for i in range(N-1, -1, -1):
            while stack and A[i] < A[stack[-1]]:
                stack.pop()
            nxt[i] = stack[-1] if stack else N
            stack.append(i)
        
        return sum([(i - prv[i])*(nxt[i] - i)*A[i] for i in range(N)]) % MOD