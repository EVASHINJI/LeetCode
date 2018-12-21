# Url: https://leetcode.com/problems/range-addition-ii/
# Related Topics:
# Math

# Example:
# Input: 
# m = 3, n = 3
# operations = [[2,2],[3,3]]
# Output: 4


class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        for op in ops:
            m = min(m, op[0])
            n = min(n, op[1])
        return m * n