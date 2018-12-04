# Url: https://leetcode.com/problems/number-of-segments-in-a-string/
# Related Topics:
# String

# Example:
# Input: "Hello, my name is John"
# Output: 5


class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev_word_flag, ans = 0, 0
        for c in s + ' ':
            if c.isspace():
                if prev_word_flag:
                    ans += 1
                prev_word_flag = 0
            else:
                prev_word_flag = 1
        return ans