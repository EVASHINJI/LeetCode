# Url: https://leetcode.com/problems/sum-of-even-numbers-after-queries/
# Related Topics:
# Array

# Example 1:
# Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
# Output: [8,6,2,4]
# Explanation: 
# At the beginning, the array is [1,2,3,4].
# After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
# After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
# After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
# After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        even = sum([a for a in A if a % 2 == 0])
        for val, idx in queries:
            if A[idx] % 2 == 0:
                even -= A[idx]
            A[idx] += val
            if A[idx] % 2 == 0:
                even += A[idx]
            ans.append(even)
        return ans