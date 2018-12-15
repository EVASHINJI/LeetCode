# Url: https://leetcode.com/problems/di-string-match/
# Related Topics:
# Math

# Example:
# Input: "IDID"
# Output: [0,4,1,3,2]


class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        i, d = 0, len(S)
        ans = []
        for c in S:
            if c == 'I':
                ans.append(i)
                i += 1
            if c == 'D':
                ans.append(d)
                d -= 1
        ans.append(i)
        return ans