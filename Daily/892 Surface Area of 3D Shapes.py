# Url: https://leetcode.com/problems/surface-area-of-3d-shapes/
# Related Topics:
# Math Geometry

# Example:
# Input: [[2,2,2],[2,1,2],[2,2,2]]
# Output: 46


class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = (len(grid) ** 2 - sum(row.count(0) for row in grid))*2
        for row in grid:
            ans += row[0] + row[-1]
            for z1, z2 in zip(row, row[1:]):
                ans += abs(z1-z2)
        for col in list(zip(*grid)):
            ans += col[0] + col[-1]
            for z1, z2 in zip(col, col[1:]):
                ans += abs(z1-z2)
        return ans
