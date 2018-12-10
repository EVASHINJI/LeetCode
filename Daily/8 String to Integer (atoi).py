# Url: https://leetcode.com/problems/string-to-integer-atoi/
# Related Topics:
# String Math

# Example:
# Input: "-91283472332"
# Output: -2147483648
# Input: "words and 987"
# Output: 0
# Input: "4193 with words"
# Output: 4193
# Input: "   -42"
# Output: -42


import re
class Solution:
    def myAtoi(self, strs):
        """
        :type str: str
        :rtype: int
        """
        match_obj = re.match('[\+\-]?[0-9]+', strs.lstrip())
        if match_obj:
            n = int(match_obj.group())
            if n < -(1 << 31):
                return -(1 << 31)
            elif n > (1 << 31) - 1:
                return (1 << 31) - 1
            return n
        else:
            return 0