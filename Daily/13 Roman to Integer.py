# Url: https://leetcode.com/problems/roman-to-integer/
# Related Topics:
# String Math

# Example:
# Input: "MCMXCIV"
# Output: 1994


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman2int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        special = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        ans, i, l = 0, 0, len(s)
        while i < l:
            if i < l - 1 and s[i] + s[i+1] in special:
                ans += special[s[i] + s[i+1]]
                i += 2
                continue
            ans += roman2int[s[i]]
            i += 1
        return ans
        