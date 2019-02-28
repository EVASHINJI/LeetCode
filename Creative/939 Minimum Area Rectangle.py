# Url: https://leetcode.com/problems/minimum-area-rectangle/
# Related Topics:
# HashTable

# Example 1:
# Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
# Example 2:
# Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2

# Creative
# Sort by column or Diagonal

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        S = set(map(tuple, points))
        ans = float('inf')
        for j, p2 in enumerate(points):
            for i in range(j):
                p1 = points[i]
                if p1[0] != p2[0] and p1[1] != p2[1] and (p1[0], p2[1]) in S and (p2[0], p1[1]) in S:
                    ans = min(ans, abs(p1[0] - p2[0])*abs(p1[1] - p2[1]))
        return ans if ans < float('inf') else 0