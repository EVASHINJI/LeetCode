# Url: https://leetcode.com/problems/reordered-power-of-2/
# Related Topics:
# Math

# Example:
# Input: 46
# Output: true


class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        N_str_sorted = sorted(str(N))
        n = 1
        while len(str(n)) <= len(N_str_sorted):
            if N_str_sorted == sorted(str(n)):
                return True
            n *= 2
        return False