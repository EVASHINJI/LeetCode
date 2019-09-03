# Url: https://leetcode.com/problems/long-pressed-name/
# Related Topics:
# String TwoPointers

# Example:
# Input: name = "saeed", typed = "ssaaedd"
# Output: false

# Creative itertools.groupby function, use package or realize by self


class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        g1 = [(k, len(list(grp))) for k, grp in itertools.groupby(name)]
        g2 = [(k, len(list(grp))) for k, grp in itertools.groupby(typed)]
        if len(g1) != len(g2):
            return False
        
        return all(k1 == k2 and v1 <= v2 for (k1, v1), (k2, v2) in zip(g1, g2))