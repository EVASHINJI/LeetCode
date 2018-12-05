# Url: https://leetcode.com/problems/ambiguous-coordinates/
# Related Topics:
# String

# Example:
# Input: "(0123)"
# Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]


class Solution:
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def generate_number(s):
            gen = []
            if s[0] != '0' or len(s) == 1:
                gen.append(s)
                
            for i in range(1, len(s)):
                f = s[:i] + '.' + s[i:]
                if f[-1] != '0' and (f[0] != '0' or i == 1):
                    gen.append(f)
            return gen
        
        ans = []
        S = S[1:-1]
        for i in range(1, len(S)):
            left, right = S[:i], S[i:]
            left_num = generate_number(left)
            right_num = generate_number(right)
            for l in left_num:
                for r in right_num:
                    ans.append('(%s, %s)' % (l, r))
        return ans