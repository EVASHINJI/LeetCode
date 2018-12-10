# Url: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Related Topics:
# String HashTable TwoPointers

# Example:
# Input: "pwwkew"
# Output: 3

# Creative record the last occur char


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, ans, start = len(s), 0, 0
        last_occur = {}
        for i, c in enumerate(s):
            if c in last_occur:
                start = max(last_occur[c], start)
            ans = max(ans, i - start + 1)
            last_occur[c] = i + 1
        return ans