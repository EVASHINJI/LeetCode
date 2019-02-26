# Url: https://leetcode.com/problems/single-number/
# Related Topics:
# HashTable BitManipulation

# Example 1:
# Input: [2,2,1]
# Output: 1
# Example 2:
# Input: [4,1,2,1,2]
# Output: 4

# Creative
# Bit Manipulation ^ - XOR
# a^0 = a   a^a = 0   a^b^a = a^a^b = 0^b = b


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for n in nums:
            a ^= n
        return a