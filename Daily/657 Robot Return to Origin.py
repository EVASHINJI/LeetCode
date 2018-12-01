# Url: https://leetcode.com/problems/robot-return-to-origin/
# Related Topics:
# String

# Example 1:
# Input: "UD"
# Output: true 


class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        inc = {'R':(1, 0), 'L':(-1, 0), 'U':(0, 1), 'D': (0, -1)}
        x, y = 0, 0
        for move in moves:
            inc_x, inc_y = inc[move]
            x, y = x + inc_x, y + inc_y
        return (x, y) == (0, 0)