# Url: https://leetcode.com/problems/sum-of-square-numbers/
# Related Topics:
# Math

# Example:
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5


import math
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        def is_square(n):
            return int(math.sqrt(n)) ** 2 == n
        
        for i in range(int(math.sqrt(c)) + 1):
            if is_square(c - i * i):
                return True
        return False