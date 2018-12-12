# Url: https://leetcode.com/problems/shortest-palindrome/
# Related Topics:
# String

# Example:
# Input: "aacecaaa"
# Output: "aaacecaaa"

# Creative 
# use KMP's idea - most similar prefix & suffix, 
# record the reversed str suffix length


class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev = ''.join(reversed(s))
        new_s = s + '#' + rev
        f = [0] * len(new_s)
        for i in range(1, len(new_s)):
            t = f[i-1]
            while t > 0 and new_s[i] != new_s[t]:
                t = f[t-1]
            if new_s[i] == new_s[t]:
                t += 1
            f[i] = t
        return rev[:len(s)-f[-1]] + s