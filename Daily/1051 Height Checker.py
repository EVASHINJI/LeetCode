# Url: https://leetcode.com/problems/height-checker/
# Related Topics:
# Array

# Example 1:
# Input: [1,1,4,2,1,3]
# Output: 3
# Explanation: 
# Students with heights 4, 3 and the last 1 are not standing in the right positions.


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        right = sorted(heights)
        ans = 0
        for i, j in zip(heights, right):
            if i != j:
                ans += 1
        return ans