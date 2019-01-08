# Url: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
# Related Topics:
# HashTable

# Example:
# Input: [1,2,3,3]
# Output: 3


class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        seen = set()
        for a in A:
            if a in seen:
                return a
            seen.add(a)