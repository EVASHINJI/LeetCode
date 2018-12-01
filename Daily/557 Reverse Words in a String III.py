# Url: https://leetcode.com/problems/reverse-words-in-a-string-iii/submissions/
# Related Topics:
# String

# Example:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"


class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([word[::-1] for word in s.split(' ')])