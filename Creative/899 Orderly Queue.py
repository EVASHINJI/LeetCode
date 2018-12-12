# Url: https://leetcode.com/problems/orderly-queue/
# Related Topics:
# String Math

# Example:
# Input: S = "baaca", K = 3
# Output: "aaabc"

# Creative notice when K > 1 we can swap any adjacent element then think about babble sort


class Solution:
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if K == 1:
            mi = min(S)
            min_S = S
            for i, c in enumerate(S):
                if c == mi:
                    min_S = min(min_S, S[i:] + S[:i])
            return min_S
        else:
            return ''.join(sorted(S))