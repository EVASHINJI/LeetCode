# Url: https://leetcode.com/problems/integer-replacement/
# Related Topics:
# Math BitManipulation

# Example:
# Input:7
# Output:4
# Explanation:
# 7 -> 8 -> 4 -> 2 -> 1
# or
# 7 -> 6 -> 3 -> 2 -> 1

# Creative
# mathematical induction. find the fomula


class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        ans = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            elif (n+1) % 4 == 0 and n != 3:
                n = n + 1
            else:
                n = n - 1
            ans += 1
        return ans