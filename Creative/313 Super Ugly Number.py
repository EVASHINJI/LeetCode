# Url: https://leetcode.com/problems/super-ugly-number/
# Related Topics:
# Math Heap

# Example:
# Input: n = 12, primes = [2,7,13,19]
# Output: 32 
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 

# Creative
# idx 表示第i个质数应该与第几个uglynum相乘
# fct 表示第m个uglynum的因子是第i个质数


import heapq
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        p = [1] * n
        fct = [0] * n
        idx = [0] * len(primes)
        pq = [(primes[i], i) for i in range(len(primes))]
        
        for m in range(1, n):
            p[m], i = heapq.heappop(pq)
            idx[i] += 1
            fct[m] = i
            while fct[idx[i]] > i:
                idx[i] += 1
            heapq.heappush(pq, (primes[i] * p[idx[i]], i))
        return p[-1]