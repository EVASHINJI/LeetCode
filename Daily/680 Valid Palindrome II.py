# Url: https://leetcode.com/problems/valid-palindrome-ii/
# Related Topics:
# String

# Example:
# Input: "abca"
# Output: True


class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_ = s[::-1]
        if s_ == s:
            return True
        for i, (x, y) in enumerate(zip(s, s_)):
            if x != y:
                new_s = s[:i] + s[i+1:]
                if new_s == new_s[::-1]:
                    return True
                
                new_s = s_[:i] + s_[i+1:]
                if new_s == new_s[::-1]:
                    return True
                return False