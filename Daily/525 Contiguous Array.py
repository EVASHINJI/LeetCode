# Url: https://leetcode.com/problems/contiguous-array/
# Related Topics:
# HashTable

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans, cnt = 0, 0
        point = {0: 0}
        for i, n in enumerate(nums, 1):
            cnt += 1 if n else -1
            if cnt in point:
                ans = max(i-point[cnt], ans)
            else:
                point[cnt] = i
        return ans