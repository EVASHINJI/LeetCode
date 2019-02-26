# Url: https://leetcode.com/problems/word-pattern/
# Related Topics:
# HashTable

# Example 1:
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# Example 2:
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false


class Solution:
    def wordPattern(self, pattern: str, str1: str) -> bool:
        str_list = str1.split(' ')
        if len(pattern) != len(str_list):
            return False
        m = {}
        for c, s in zip(pattern, str_list):
            s += '#'
            if (c in m and m[c] != s) or (s in m and m[s] != c):
                return False
            m[c] = s
            m[s] = c
        return True