# Url: https://leetcode.com/problems/minimum-increment-to-make-array-unique/
# Related Topics:
# Array

# Example 1:
# Input: [1,2,2]
# Output: 1
# Explanation:  After 1 move, the array could be [1, 2, 3].

# Example 2:
# Input: [3,2,1,2,1,7]
# Output: 6
# Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
# It can be shown with 5 or less moves that it is impossible for the array to have all unique values.


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        count = collections.Counter(A)
        taken = []
        
        ans = 0
        for x in range(100000):
            if count[x] > 1:
                taken.extend([x] * (count[x] - 1))
            elif taken and count[x] == 0:
                ans += x - taken.pop()
        return ans