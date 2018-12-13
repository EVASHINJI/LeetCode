# Url: https://leetcode.com/problems/wildcard-matching/
# Related Topics:
# String DP BackTracking Greedy

# Example:
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        l_s, l_p = len(s), len(p)
        dp = [[False] * (l_s + 1) for _ in range(l_p + 1)]
        dp[0][0] = True
        for i in range(1, l_p + 1):
            for j in range(l_s + 1):
                if j == 0:
                    if p[i-1] == '*':
                        dp[i][0] = dp[i-1][0]
                    continue
                if p[i-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                elif p[i-1] == '?' or p[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]
            