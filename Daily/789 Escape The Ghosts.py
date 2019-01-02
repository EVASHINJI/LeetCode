# Url: https://leetcode.com/problems/escape-the-ghosts/
# Related Topics:
# Math

# Example:
# Input: 
# ghosts = [[1, 0], [0, 3]]
# target = [0, 1]
# Output: true
# Explanation: 
# You can directly reach the destination (0, 1) at time 1, 
# while the ghosts located at (1, 0) or (0, 3) have no way to catch up with you.


class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        my_step = abs(target[0]) + abs(target[1])
        for i in range(len(ghosts)):
            if abs(target[0] - ghosts[i][0]) + abs(target[1] - ghosts[i][1]) <= my_step:
                return False
        return True
            