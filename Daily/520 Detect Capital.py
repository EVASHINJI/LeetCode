# Url: https://leetcode.com/problems/detect-capital/
# Related Topics:
# String

# Example:
# Input: "FlaG"
# Output: False


class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def all_capitals(s):
            for c in s:
                if not 'A' <= c <= 'Z':
                    return False
            return True
        
        def all_not_capitals(s):
            for c in s:
                if not 'a' <= c <= 'z':
                    return False
            return True
        
        return all_capitals(word) or all_not_capitals(word) or (all_capitals(word[0]) and all_not_capitals(word[1:]))