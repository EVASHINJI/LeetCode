# Url: https://leetcode.com/problems/reorder-log-files/
# Related Topics:
# String

# Example:
# Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]


class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def keys(log):
            _id, rest = log.split(' ', 1)
            return (0, rest, _id) if rest[0].isalpha() else (1,)
        
        return sorted(logs, key=keys)