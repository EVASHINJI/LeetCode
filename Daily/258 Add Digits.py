# Url: https://leetcode.com/problems/add-digits/
# Related Topics:
# Math

# Example:
# Input: 38
# Output: 2 


class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            d, tmp = num, 0
            while d:
                d, m = divmod(d, 10)
                tmp += m
            num = tmp
        return num