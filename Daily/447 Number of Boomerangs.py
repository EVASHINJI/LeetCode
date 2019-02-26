# Url: https://leetcode.com/problems/number-of-boomerangs/
# Related Topics:
# HashTable

# Example:
# Input:
# [[0,0],[1,0],[2,0]]
# Output:
# 2
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def distance(x, y):
            return (x[0] - y[0])**2 + (x[1] - y[1])**2
        ans = 0
        for p in points:
            dis_map = {}
            for q in points:
                dis = distance(p, q)
                dis_map[dis] = dis_map.get(dis, 0) + 1
            for v in dis_map.values():
                ans += v * (v - 1)
        return ans