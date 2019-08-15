# Url: https://leetcode.com/problems/add-to-array-form-of-integer/
# Related Topics:
# Array 

# Example 1:
# Input: A = [1,2,0,0], K = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234

# Example 2:
# Input: A = [2,7,4], K = 181
# Output: [4,5,5]
# Explanation: 274 + 181 = 455


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A[-1] += K
        for i in range(len(A) - 1, 0, -1):
            ad, A[i] = divmod(A[i], 10)
            A[i-1] += ad
            if ad == 0:
                break
        if A[0] >= 10:
            return list(map(int, str(A[0]))) + A[1:]
        return A
            