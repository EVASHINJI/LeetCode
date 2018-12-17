# Url: https://leetcode.com/problems/excel-sheet-column-title/
# Related Topics:
# Math

# Example:
# Input: 28
# Output: "AB"


class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ''
        while n != 0:
            n, m = divmod(n, 26)
            if m == 0:
                n -= 1
                m = 26
            ans += chr(ord('A') + m - 1)
        return ans[::-1]