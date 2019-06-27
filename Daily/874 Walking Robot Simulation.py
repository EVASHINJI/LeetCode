# Url: https://leetcode.com/problems/walking-robot-simulation/
# Related Topics:
# Greedy

# Example 1:
# Input: commands = [4,-1,3], obstacles = []
# Output: 25
# Explanation: robot will go to (3, 4)
# Example 2:
# Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# Output: 65
# Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)



class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set(map(tuple, obstacles))
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, d = 0, 0, 0
        ans = 0
        for cmd in commands:
            if cmd == -1:
                d = (d+1) % 4
            elif cmd == -2:
                d = (d+3) % 4
            else:
                dx, dy = direction[d]
                for _ in range(cmd):
                    if (x + dx, y + dy) not in obs:
                        x, y = x + dx, y + dy
                    else:
                        break
                ans = max(ans, x*x + y*y)
        return ans
        
        