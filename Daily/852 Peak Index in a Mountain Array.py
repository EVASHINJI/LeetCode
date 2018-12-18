# Url: https://leetcode.com/problems/peak-index-in-a-mountain-array/
# Related Topics:
# BinarySearch

# Example:
# Input: [0,2,1,0]
# Output: 1


class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))