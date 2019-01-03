# Url: https://leetcode.com/problems/bulb-switcher/
# Related Topics:
# Math Brainteaser

# Example:
# Input: 3
# Output: 1 
# Explanation: 
# At first, the three bulbs are [off, off, off].
# After first round, the three bulbs are [on, on, on].
# After second round, the three bulbs are [on, off, on].
# After third round, the three bulbs are [on, off, off]. 


import math
class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))
