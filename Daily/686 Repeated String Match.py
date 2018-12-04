# Url: https://leetcode.com/problems/repeated-string-match/
# Related Topics:
# String

# Example:
# Input: "abc"
# Output: "cabcabca"


class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        times = math.ceil(len(B) / len(A))
        for t in range(times, times + 2):
            if B in A*t:
                return t
        return -1