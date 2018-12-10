# Url: https://leetcode.com/problems/optimal-division/
# Related Topics:
# String Math

# Example:
# Input: [1000,100,10,2]
# Output: "1000/(100/10/2)"


class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        A = list(map(str, nums))
        if len(A) <= 2:
            return '/'.join(A)
        return A[0] + '/(' + '/'.join(A[1:]) + ')'