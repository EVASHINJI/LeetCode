# Url: https://leetcode.com/problems/can-make-palindrome-from-substring/
# Related Topics:
# String Array

# Example :
# Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
# Output: [true,false,false,true,true]
# Explanation:
# queries[0] : substring = "d", is palidrome.
# queries[1] : substring = "bc", is not palidrome.
# queries[2] : substring = "abcd", is not palidrome after replacing only 1 character.
# queries[3] : substring = "abcd", could be changed to "abba" which is palidrome. Also this can be changed to "baab" first rearrange it "bacd" then replace "cd" with "ab".
# queries[4] : substring = "abcda", could be changed to "abcba" which is palidrome.

# Creative
# 逐步优化内存，通过数组相减得到每个区间的统计，最后用bits来表示存储的数，用异或来计算差异，降低内存开销，要好好研究一下位存储了

from collections import Counter
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        num = [ord(ch) - ord('a') for ch in s]
        dp = [0]
        for n in num:
            dp.append(dp[-1] ^ (1 << n))
        return [bin(dp[r+1] ^ dp[l]).count('1') >> 1 <= k for l, r, k in queries]