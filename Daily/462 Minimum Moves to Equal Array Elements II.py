# Url: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
# Related Topics:
# Math

# Example:
# Input: [1,2,3]
# Output: 2
# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]


class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        median = sorted(nums)[len(nums) // 2]
        return sum([abs(n - median) for n in nums])