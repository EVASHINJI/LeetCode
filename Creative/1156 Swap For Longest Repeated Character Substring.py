# Url: https://leetcode.com/problems/swap-for-longest-repeated-character-substring/
# Related Topics:
# String

# Example 1:
# Input: text = "ababa"
# Output: 3
# Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa", which its length is 3.

# Example 2:
# Input: text = "aaabaaa"
# Output: 6
# Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa", which its length is 6.

# Example 3:
# Input: text = "aaabbaaa"
# Output: 4

# Creative
# Don't want to get the ans in once.


from itertools import groupby
from collections import Counter
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        cnt = Counter(text)
        grp = [(k, len(list(g))) for k, g in groupby(text)]
        ans = max([min(g+1, cnt[k]) for k, g in grp])
        for i in range(1, len(grp)-1):
            if grp[i-1][0] == grp[i+1][0] and grp[i][1] == 1:
                ans = max(min([cnt[grp[i-1][0]], grp[i-1][1] + 1 + grp[i+1][1]]), ans)
        return ans