# Url: https://leetcode.com/problems/isomorphic-strings/
# Related Topics:
# HashTable

# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
# Input: s = "paper", t = "title"
# Output: true


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        seen = {}
        for c1, c2 in zip(s, t):
            if c1 in mapping and mapping[c1] != c2:
                return False
            if c2 in seen and seen[c2] != c1:
                return False
            seen[c2] = c1
            mapping[c1] = c2
        return True