# Url: https://leetcode.com/problems/longest-arithmetic-sequence/
# Related Topics:
# DP

# Example 1:
# Input: [3,6,9,12]
# Output: 4
# Explanation: 
# The whole array is an arithmetic sequence with steps of length = 3.

# Example 2:
# Input: [9,4,7,2,10]
# Output: 3
# Explanation: 
# The longest arithmetic subsequence is [4,7,10].


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A:
            return 0
        dp = {}
        seen = set()
        for a in A:
            for before in seen:
                delta = a - before
                nxt = a + delta
                dp[(nxt + delta, delta)] = dp.get((nxt, delta), 1) + 1
            seen.add(a)
        return max(dp.values())