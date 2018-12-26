# Url: https://leetcode.com/problems/count-primes/
# Related Topics:
# Math

# Example:
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# Creative
# sometimes list is better than set, expecially know the index
# and the lower factor has been masked, we can find the better start
# such as 5*1 5*2 has been masked by 1 2, we can start from 5


import math
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        primes = [True] * n
        for i in range(2, int(math.sqrt(n))+1):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False
        primes[0], primes[1] = False, False
        return sum(primes)