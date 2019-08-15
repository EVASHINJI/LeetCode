# Url: https://leetcode.com/problems/binary-prefix-divisible-by-5/
# Related Topics:
# Array

# Example 1:
# Input: [0,1,1]
# Output: [true,false,false]
# Explanation: 
# The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is divisible by 5, so answer[0] is true.

# Example 2:
# Input: [1,1,1]
# Output: [false,false,false]


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        num = 0
        ans = []
        for a in A:
            num = num*2 + a
            if num % 5:
                ans.append(False)
            else:
                ans.append(True)
        return ans