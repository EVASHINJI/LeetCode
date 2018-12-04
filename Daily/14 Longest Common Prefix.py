# Url: https://leetcode.com/problems/longest-common-prefix/
# Related Topics:
# String

# Example:
# Input: ["flower","flow","flight"]
# Output: "fl"


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        max_l = len(strs[0])
        prefix = {i:c for i, c in enumerate(strs[0])}
        for s in strs:
            max_l = min(max_l, len(s))
            for i in range(max_l):
                if prefix[i] != s[i]:
                    max_l = i
                    break
            if max_l == 0:
                return ""
        return strs[0][:max_l]