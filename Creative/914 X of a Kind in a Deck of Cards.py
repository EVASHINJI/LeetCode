# Url: https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
# Related Topics:
# Math Array

# Example:
# Input: [1,1,2,2,2,2]
# Output: true

# Creative
# Review the Greatest Common Divisor


from collections import Counter
from functools import reduce
class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(a, b):
            ma, mi = max(a, b), min(a, b)
            if mi == 0:
                return ma
            return gcd(mi, ma % mi)
        
        cnt = Counter(deck)
        ans = reduce(gcd, cnt.values())
        return ans >= 2