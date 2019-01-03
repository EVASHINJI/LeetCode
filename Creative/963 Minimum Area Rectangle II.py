# Url: https://leetcode.com/problems/minimum-area-rectangle-ii/
# Related Topics:
# Math Geometry

# Example:
# Input: [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
# Output: 2.00000
# Explanation: The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.

# Creative
# Iterate Centers
# complex's abs is a+bi * a-bi


import itertools, collections
class Solution(object):
    def minAreaFreeRect(self, points):
        points = [complex(*z) for z in points]
        seen = collections.defaultdict(list)
        for P, Q in itertools.combinations(points, 2):
            center = (P + Q) / 2
            radius = abs(center - P)
            seen[center, radius].append(P)

        ans = float("inf")
        for (center, radius), candidates in seen.items():
            for P, Q in itertools.combinations(candidates, 2):
                ans = min(ans, abs(P - Q) * abs(P - (2*center - Q)))

        return ans if ans < float("inf") else 0