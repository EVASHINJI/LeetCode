# Url: https://leetcode.com/problems/zigzag-conversion/
# Related Topics:
# String

# Example:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        ans = ""
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                shift = (2 * numRows - 2, 2 * numRows - 2)
            else:
                shift = (2 * (numRows - 1 - i), 2 * i)
            idx, flag = i, 0
            while idx < len(s):
                ans += s[idx]
                idx += shift[flag]
                flag ^= 1
        return ans