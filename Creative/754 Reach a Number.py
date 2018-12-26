# Url: https://leetcode.com/problems/reach-a-number/
# Related Topics:
# Math

# Example:
# Input: target = 2
# Output: 3
# Explanation:
# On the first move we step from 0 to 1.
# On the second move we step  from 1 to -1.
# On the third move we step from -1 to 2.

# Creative
# find the smallest sum and change the sign


import math
class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        k = int(math.sqrt(2*target))
        S = k * (k + 1) / 2
        while S < target:
            k += 1
            S += k
        while (S - target) % 2 != 0:
            k += 1
            S += k
        return k
        