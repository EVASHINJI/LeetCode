# Url: https://leetcode.com/problems/rectangle-overlap/
# Related Topics:
# Math

# Example:
# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# Output: false


class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x11, y11, x12, y12 = rec1
        x21, y21, x22, y22 = rec2
        return not (y11 >= y22 or y12 <= y21 or x11 >= x22 or x12 <= x21)