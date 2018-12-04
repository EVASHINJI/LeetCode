# Url: https://leetcode.com/problems/first-unique-character-in-a-string/
# Related Topics:
# String HashTabel

# Example:
# Input: "loveleetcode"
# Output: 2


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        for c in s:
            if c not in seen:
                l, r = s.find(c), s.rfind(c)
                if l == r:
                    return l
                seen.add(c)
        return -1