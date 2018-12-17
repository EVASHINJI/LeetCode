# Url: https://leetcode.com/problems/ugly-number/
# Related Topics:
# Math

# Example:
# Input: 8
# Output: true


class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        if num == 1:
            return True
        while num not in [2,3,5]:
            for i in [2, 3, 5]:
                if num % i == 0:
                    num = num // i
                    break
            else:
                return False
        return True