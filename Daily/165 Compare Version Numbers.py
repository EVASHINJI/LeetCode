# Url: https://leetcode.com/problems/compare-version-numbers/
# Related Topics:
# String

# Example:
# Input: version1 = "0.1", version2 = "1.1"
# Output: -1


class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1, version2 = version1.split('.'), version2.split('.')
        max_l = max(len(version1), len(version2))
        version1.extend([0] * (max_l - len(version1)))
        version2.extend([0] * (max_l - len(version2)))
        for v1, v2 in zip(version1, version2):
            v1, v2 = int(v1), int(v2)
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0
        