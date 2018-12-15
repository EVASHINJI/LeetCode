# Url: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
# Related Topics:
# Math

# Example:
# Input: [1,2,3]
# Output: 3


class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums) * len(nums)