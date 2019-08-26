# Url: https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Related Topics:
# String

# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        pattern = str1 if l1 < l2 else str2
        for i in range(len(pattern), 0, -1):
            x = pattern[:i]
            lx = len(x)
            if l1 % lx or l2 % lx:
                continue
            if str1 == x * (l1//lx) and str2 == x*(l2//lx):
                return x
        return ""