# Url: https://leetcode.com/problems/island-perimeter/
# Related Topics:
# HashTable

# Example:
# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
# Output: 16


from collections import defaultdict
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        edge = defaultdict(lambda: 0)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    for d in [-0.5, 0.5]:
                        edge[(i+d, j)] += 1
                        edge[(i, j+d)] += 1
        return sum([v for v in edge.values() if v == 1])