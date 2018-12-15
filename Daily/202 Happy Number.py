# Url: https://leetcode.com/problems/happy-number/
# Related Topics:
# Math HashTable

# Example:
# Input: 19
# Output: true


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        happy, seen = n, set([n])
        while happy != 1:
            happy = sum(map(lambda x: int(x)**2, str(happy)))
            if happy in seen:
                return False
            seen.add(happy)
        return True