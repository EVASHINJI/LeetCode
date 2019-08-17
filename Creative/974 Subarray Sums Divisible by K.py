# Url: https://leetcode.com/problems/subarray-sums-divisible-by-k/
# Related Topics:
# Array HashTable

# Example 1:
# Input: A = [4,5,0,-2,-3,1], K = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by K = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        sum_A = [0]
        for a in A:
            sum_A.append((sum_A[-1] + a) % K)
        cnt = collections.Counter(sum_A)
        return int(sum(v*(v-1)/2 for v in cnt.values()))