# Url: https://leetcode.com/problems/permutation-sequence/
# Related Topics:
# Math Backtracking

# Example:
# Input: n = 4, k = 9
# Output: "2314"

# Creative
# It's not necessary to enumerate every permutations.
# We can find the rule of permutation and skip it.


import math
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = list(range(1, n+1))
        permutation = ""
        k -= 1
        while n > 0:
            n -= 1
            idx, k = divmod(k, math.factorial(n))
            permutation += str(nums[idx])
            nums.remove(nums[idx])
        return permutation