# Url: https://leetcode.com/problems/count-binary-substrings/
# Related Topics:
# String

# Example:
# Input: "00110011"
# Output: 6


class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur , 1
            else:
                cur += 1
        return ans + min(prev, cur)
            