# Url: https://leetcode.com/problems/ransom-note/
# Related Topics:
# String

# Example:
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true


from collections import Counter
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cnt = Counter(magazine)
        for letter in ransomNote:
            if letter not in magazine or not cnt[letter]:
                return False
            cnt[letter] -= 1
        return True