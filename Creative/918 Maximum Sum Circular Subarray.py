# Url: https://leetcode.com/problems/maximum-sum-circular-subarray/
# Related Topics:
# Array

# Example 1:
# Input: [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3

# Example 2:
# Input: [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        p = [0]
        N = len(A)
        for a in A + A:
            p.append(p[-1] + a)
            
        deque = collections.deque([0])
        ans = A[0]
        for i in range(1, len(p)):
            if i - deque[0] > N:
                deque.popleft()
                
            ans = max(ans, p[i] - p[deque[0]])
            
            while deque and p[i] <= p[deque[-1]]:
                deque.pop()
            
            deque.append(i)
        return ans