# Url: https://leetcode.com/problems/delete-columns-to-make-sorted/
# Related Topics:
# Greedy

# Example 1:
# Input: ["cba","daf","ghi"]
# Output: 1
# Explanation: 
# After choosing D = {1}, each column ["c","d","g"] and ["a","f","i"] are in non-decreasing sorted order.
# If we chose D = {}, then a column ["b","a","h"] would not be in non-decreasing sorted order.
# Example 2:
# Input: ["a","b"]
# Output: 0
# Explanation: D = {}


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        if not A:
            return 0
        D = 0
        for j in range(len(A[0])):
            for i in range(1, len(A)):
                if A[i][j] < A[i-1][j]:
                    D += 1
                    break
        return D