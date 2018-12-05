# Url: https://leetcode.com/problems/minimum-time-difference/
# Related Topics:
# String

# Example:
# Input: ["23:59","00:00"]
# Output: 1


class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        time_points = []
        added = set()
        for time in timePoints:
            h, m = int(time[:2]), int(time[3:5])
            minutes = 60 * h + m
            time_points.append(minutes)
            if h < 12:
                added.add(minutes + 1440)
        time_points += list(added)
        time_points.sort()
        min_diff = 1440
        for i in range(len(time_points)):
            for j in range(i + 1, len(time_points)):
                if time_points[j] - time_points[i] < min_diff:
                    min_diff = time_points[j] - time_points[i]
                else:
                    break
        return min_diff