# Url: https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
# Related Topics:
# Array

# Example 1:
# Input: [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

# Example 2:
# Input: [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sum_A = sum(A)
        if sum_A % 3 == 0:
            even = sum_A / 3
            i = 0
            temp = 0
            for a in A:
                temp += a
                if temp == even:
                    i += 1
                    temp = 0
                    if i == 2:
                        return True
        return False