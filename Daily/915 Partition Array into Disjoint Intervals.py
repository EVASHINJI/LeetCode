# Url: https://leetcode.com/problems/partition-array-into-disjoint-intervals/
# Related Topics:
# Array

# Example 1:
# Input: [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]

# Example 2:
# Input: [1,1,1,0,6,12]
# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]


class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:  
        cur_max, temp_max = A[0], A[0]
        ans = 1
        for i in range(1, len(A)):
            if A[i] < cur_max:
                cur_max, ans = temp_max, i + 1
            elif A[i] > temp_max:
                temp_max = A[i]
        return ans