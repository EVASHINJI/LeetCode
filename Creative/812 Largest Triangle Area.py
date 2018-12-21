# Url: https://leetcode.com/problems/largest-triangle-area/
# Related Topics:
# Math

# Example:
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2

# Creative
# Shoelace formula


class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def Area(a, b, c):
            x1, y1 = a
            x2, y2 = b
            x3, y3 = c
            return 0.5 * abs(x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3)
        
        max_area = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    max_area = max(Area(points[i], points[j], points[k]), max_area)
        
        return max_area