# Url: https://leetcode.com/problems/longest-uncommon-subsequence-ii/
# Related Topics:
# String

# Example:
# Input: "aba", "cdc", "eae"
# Output: 3

# Creative the way to judge if s1 is the subseqence of s2


from collections import Counter
class Solution:
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def subseq(s1, s2):
            if len(s1) > len(s2):
                return 0
            
            i = 0
            for c in s2:
                if i < len(s1) and s1[i] == c:
                    i += 1
            return i == len(s1)
        
        dic = sorted(Counter(strs).items(), key=lambda x: (-len(x[0]), x[1]))
        
        strs.sort(key=len, reverse=True)
        for i, s1 in enumerate(dic):
            if s1[1] > 1:
                continue
            if not any(subseq(s1[0], s2[0]) for j, s2 in enumerate(dic) if i != j):
                return len(s1[0])
        return -1
                