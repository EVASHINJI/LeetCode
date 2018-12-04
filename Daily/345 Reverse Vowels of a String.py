# Url: https://leetcode.com/problems/reverse-vowels-of-a-string/
# Related Topics:
# String TwoPointers

# Example:
# Input: "leetcode"
# Output: "leotcede"


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        vowels = 'aeiouAEIOU'
        vow_idx = [i for i, c in enumerate(s) if c in vowels]
        l, r = 0, len(vow_idx) - 1
        s = list(s)
        while l < r:
            s[vow_idx[l]], s[vow_idx[r]] = s[vow_idx[r]], s[vow_idx[l]]
            l, r = l + 1, r - 1
        return ''.join(s)
        