# Url: https://leetcode.com/problems/masking-personal-information/
# Related Topics:
# String

# Example:
# Input: "LeetCode@LeetCode.com"
# Output: "l*****e@leetcode.com"
# Input: "1(234)567-890"
# Output: "***-***-7890"


import re
class Solution:
    def maskPII(self, s):
        """
        :type S: str
        :rtype: str
        """
        if '@' in s:
            s = s.lower()
            prefix, postfix = s.split('@')
            prefix = prefix[0] + '*****' + prefix[-1]
            return prefix + '@' + postfix
        else:
            s = [c for c in s if c.isdigit()]
            phone = '***-***-' + ''.join(s[-4:])
            country_code = ''
            if len(s) > 10:
                country_code = '+' + ''.join('*' * (len(s) - 10)) + '-'
            return country_code + phone
                