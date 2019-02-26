# Url: https://leetcode.com/problems/longest-palindrome/
# Related Topics:
# HashTable

# Example:
# Input:
# "abccccdd"
# Output:
# 7
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.


from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        num = 0
        print(sorted(cnt.values(), reverse=True))
        for v in sorted(cnt.values(), reverse=True):
            if v % 2 == 0:
                num += v
            elif num % 2 == 0:
                num += v
            else:
                num += v - 1
        return num