# Url: https://leetcode.com/problems/squares-of-a-sorted-array/
# Related Topics:
# Array TwoPointer

# Example 1:
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Example 2:
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        N = len(A)
        j = 0
        for i in range(N):
            if A[j] < 0:
                j = i
            else:
                break
        i = j - 1
        
        ans = []
        while i >= 0 and j < N:
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else:
                ans.append(A[j]**2)
                j += 1
        while i >= 0:
            ans.append(A[i]**2)
            i -= 1
        while j < N:
            ans.append(A[j]**2)
            j += 1
        return ans