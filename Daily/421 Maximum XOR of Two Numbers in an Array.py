# Url: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
# Related Topics:
# Trie BitManipulation

# Example:
# Input: [3, 10, 5, 25, 2, 8]
# Output: 28
# Explanation: The maximum result is 5 ^ 25 = 28.


from collections import defaultdict
from functools import reduce

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        END = True
        
        ans = 0
        for i, num in enumerate(nums):
            ori = bin(num)[2:]
            ori = '0' * (32-len(ori)) + ori
            reduce(dict.__getitem__, ori, trie)[END] = i
            root = trie
            for bit in ori:
                opposite = '1' if bit == '0' else '0'
                root = root[opposite] if opposite in root else root[bit]
            ans = max(ans, num ^ nums[root[END]])
        return ans