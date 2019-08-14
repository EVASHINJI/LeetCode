# Url: https://leetcode.com/problems/duplicate-zeros/
# Related Topics:
# Array

# Example 1:
# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

# Example 2:
# Input: [1,2,3]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,2,3]


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        offset = arr.count(0)
        N = len(arr)
        for i in range(N-1, -1, -1):
            if i + offset < N:
                arr[i+offset] = arr[i]
            if arr[i] == 0:
                offset -= 1
                if i + offset < N:
                    arr[i+offset] = 0