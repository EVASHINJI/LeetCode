# Url: https://leetcode.com/problems/projection-area-of-3d-shapes/
# Related Topics:
# Math

# Example:
# Input: [[1,1,1],[1,0,1],[1,1,1]]
# Output: 14

# Creative
# only count the max num in every dimension


class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        xy = len(grid) ** 2 - sum(row.count(0) for row in grid)
        yz = sum(map(max, list(zip(*grid))))
        zx = sum(map(max, grid))
        return xy + yz + zx