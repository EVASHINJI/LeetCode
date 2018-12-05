# Url: https://leetcode.com/problems/delete-operation-for-two-strings/
# Related Topics:
# String

# Example:
# Input: "sea", "eat"
# Output: 2


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1) + 1, len(word2) + 1
        dp = [[0] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return m + n - 2 - 2*dp[-1][-1]