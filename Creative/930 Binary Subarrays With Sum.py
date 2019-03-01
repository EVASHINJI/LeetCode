# Url: https://leetcode.com/problems/binary-subarrays-with-sum/
# Related Topics:
# HashTable TwoPointers

# Example:
# Input: A = [1,0,1,0,1], S = 2
# Output: 4

# Creative
# count the num we meet in future, when we meet the subarrays' num is the count we meet before

from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        prev_sum = [0]
        for a in A: prev_sum.append(prev_sum[-1] + a)
        count = defaultdict(lambda: 0)
        ans = 0
        for x in prev_sum:
            ans += count[x]
            count[x + S] += 1
        return ans