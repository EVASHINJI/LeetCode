# Url: https://leetcode.com/problems/find-the-closest-palindrome/
# Related Topics:
# String

# Example:
# Input: "123"
# Output: "121"


class Solution:
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        l = len(n)
        cand = set()
        cand.add(10**(l-1)-1)
        cand.add(10**l+1)
        cand.add(int(n[0] * l))
        prefix = int(n[:(l+1)//2])
        for p in (-1, 0, 1):
            p = str(prefix + p)
            if l % 2:
                cand.add(int(p + p[:-1][::-1]))
            else:
                cand.add(int(p + p[::-1]))
        n = int(n)
        mi, ans = n, 0
        for x in cand:
            diff = abs(n-x)
            if diff and (diff < mi or diff == mi and x < ans):
                ans, mi = x, diff
        return str(ans)