# Url: https://leetcode.com/problems/longest-harmonious-subsequence/
# Related Topics:
# HashTable

# Example:
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].


import itertools
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        prev = None
        ans = 0
        for key, grp in itertools.groupby(nums):
            grp = len(list(grp))
            if prev:
                if key - prev[0] == 1:
                    ans = max(ans, prev[1] + grp)
            prev = (key, grp)
        return ans