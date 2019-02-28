# Url: https://leetcode.com/problems/4sum-ii/
# Related Topics:
# HashTable BinarySearch

# Example:
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
# Output: 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

# Creative
# use BinarySearch to decrease the exponential and use dict to the candidate of each list

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        def list2hist(l):
            out = {}
            for n in l:
                out[n] = out[n] + 1 if n in out else 1
            return out

        def sum_2hists(h1, h2):
            out = {}
            for n1 in h1:
                for n2 in h2:
                    n = n1 + n2
                    out[n] = out[n] + h1[n1] * h2[n2] if n in out else h1[n1] * h2[n2]
            return out
        
        sum_AB = sum_2hists(list2hist(A), list2hist(B))
        hist_C, hist_D = list2hist(C), list2hist(D)
        ans = 0
        for n1 in hist_C:
            for n2 in hist_D:
                if -n1-n2 in sum_AB:
                    ans += hist_C[n1]*hist_D[n2]*sum_AB[-n1-n2]
        return ans