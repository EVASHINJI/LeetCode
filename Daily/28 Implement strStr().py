# Url: https://leetcode.com/problems/implement-strstr/
# Related Topics:
# String TwoPointers

# Example:
# Input: haystack = "hello", needle = "ll"
# Output: 2


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l = len(needle)
        if not l:
            return 0
        if l > len(haystack):
            return -1
        for i, c in enumerate(haystack):
            if c == needle[0] and haystack[i:i+l] == needle:
                return i
        return -1