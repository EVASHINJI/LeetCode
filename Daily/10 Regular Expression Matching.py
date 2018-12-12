# Url: https://leetcode.com/problems/regular-expression-matching/
# Related Topics:
# String DP BackTracking

# Example:
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true

# Please first think of DP


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        l_s, l_p = len(s), len(p)
        dp = [[False] * (l_s + 1) for _ in range(l_p+1)]
        dp[0][0] = True
        for i in range(1, l_p + 1):
            if p[i-1] == '*':
                dp[i][0] = dp[i-2][0]
            for j in range(1, l_s + 1):
                if p[i-1].isalpha():
                    dp[i][j] = dp[i-1][j-1] and p[i-1] == s[j-1]
                elif p[i-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    dp[i][j] = dp[i-2][j] or dp[i-1][j] or (dp[i][j-1] and (p[i-2] == '.' or p[i-2] == s[j-1]))
        return dp[-1][-1]
        