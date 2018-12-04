# Url: https://leetcode.com/problems/add-binary/
# Related Topics:
# String

# Example:
# Input: a = "1010", b = "1011"
# Output: "10101"


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a, len_b = len(a), len(b)
        a, b = a[::-1], b[::-1]
        ans = ""
        i, j, inc = 0, 0, 0
        while i < len_a or j < len_b:
            i_a = int(a[i]) if i < len_a else 0
            j_b = int(b[j]) if j < len_b else 0
            cur = i_a + j_b + inc
            inc, cur = cur // 2, cur % 2
            ans += str(cur)
            i += 1
            j += 1
        if inc:
            ans += str(inc)
        return ans[::-1]
        