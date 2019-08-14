# Url: https://leetcode.com/problems/find-common-characters/
# Related Topics:
# Array HashTable

# Example 1:
# Input: ["bella","label","roller"]
# Output: ["e","l","l"]

# Example 2:
# Input: ["cool","lock","cook"]
# Output: ["c","o"]


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        common = set(A[0])
        for word in A:
            common &= set(word)
            
        ans_cnt = {}
        for word in A:
            for c in common:
                if c not in ans_cnt:
                    ans_cnt[c] = word.count(c)
                else:
                    ans_cnt[c] = min(word.count(c), ans_cnt[c])
        
        ans = []
        for c in ans_cnt:
            ans += [c] * ans_cnt[c]
        return ans