# Url: https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/
# Related Topics:
# String

# Example 1:
# Input: S = "0110", N = 3
# Output: true

# Example 2:
# Input: S = "0110", N = 4
# Output: false


class Solution:
    def queryString(self, S: str, N: int) -> bool:
        return all(bin(i)[2:] in S for i in range(N, N//2, -1))