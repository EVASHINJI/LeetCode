# Url: https://leetcode.com/problems/custom-sort-string/
# Related Topics:
# String

# Example:
# Input: S = "cba" T = "abcd"
# Output: "cbad"

class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        mapping = {c: i for i, c in enumerate(S)}
        in_s, not_in_s = [], []
        for c in T:
            if c in S:
                in_s.append(c)
            else:
                not_in_s.append(c)
        in_s.sort(key=lambda x: mapping[x])
        return ''.join(in_s + not_in_s)