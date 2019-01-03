# Url: https://leetcode.com/problems/valid-square/
# Related Topics:
# Math

# Example:
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True


class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def distance_square(a, b):
            return (a[0] - b[0])**2 + (a[1] - b[1])**2
        
        dis = sorted([distance_square(p1, p2), distance_square(p1, p3), distance_square(p1, p4), distance_square(p2, p3), distance_square(p2, p4), distance_square(p3, p4)])
        return dis[0] > 0 and dis[0] == dis[1] == dis[2] == dis[3] and dis[4] == dis[5] and dis[0] + dis[1] == dis[4]
