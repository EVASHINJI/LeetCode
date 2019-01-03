# Url: https://leetcode.com/problems/super-pow/
# Related Topics:
# Math

# Example:
# Input: a = 2, b = [3]
# Output: 8


import random
class Solution:
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if not b:
            return 1
        return pow(a, b.pop(), 1337) * self.superPow(pow(a, 10, 1337), b) % 1337
            