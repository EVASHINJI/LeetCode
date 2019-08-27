# Url: https://leetcode.com/problems/camelcase-matching/
# Related Topics:
# String Trie

# Example 1:
# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
# Output: [true,false,true,true,false]
# Explanation: 
# "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
# "FootBall" can be generated like this "F" + "oot" + "B" + "all".
# "FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".

# Example 2:
# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
# Output: [true,false,true,false,false]
# Explanation: 
# "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
# "FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = []
        lp = len(pattern)
        for q in queries:
            lq = len(q)
            i, j = 0, 0
            while i < lq:
                if j < lp and q[i] == pattern[j]:
                    i += 1
                    j += 1
                    continue
                if q[i] == q[i].lower():
                    i += 1
                else:
                    break
            ans.append(i == lq and j == lp)
        return ans