# Url: https://leetcode.com/problems/brick-wall/
# Related Topics:
# HashTable

# Example:
# Input: [[1,2,2,1],
#         [3,1,2],
#         [1,3,2],
#         [2,4],
#         [3,1,2],
#         [1,3,1,1]]
# Output: 2


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gap_cnt = {'egde': 0}
        for i in range(len(wall)):
            gap = 0
            for j in range(len(wall[i])-1):
                gap += wall[i][j]
                gap_cnt[gap] = gap_cnt.get(gap, 0) + 1
        return len(wall) - max(gap_cnt.values())