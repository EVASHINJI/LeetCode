# Url: https://leetcode.com/problems/repeated-dna-sequences/
# Related Topics:
# HashTable BitManipulation

# Example:
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC", "CCCCCAAAAA"]


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        patterns, ans = set(), set()
        for i in range(len(s) - 9):
            p = s[i:i+10]
            if p not in patterns:
                patterns.add(p)
            elif p not in ans:
                ans.add(p)
        return list(ans)