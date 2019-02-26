# Url: https://leetcode.com/problems/find-the-difference/
# Related Topics:
# HashTable BitManipulation

# Example:
# Input:
# s = "abcd"
# t = "abcde"
# Output:
# e
# Explanation:
# 'e' is the letter that was added.


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # return chr(sum(map(ord, t)) - sum(map(ord, s)))
        a = 0
        for i in s+t:
            a ^= ord(i)
        return chr(a)