# Url: https://leetcode.com/problems/generate-parentheses/
# Related Topics:
# String BackTrack

# Example:
# Input: 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Creative backtrack way or recursion


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2*n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(', left + 1, right)
            if right < left:
                backtrack(S+')', left, right + 1)
        
        backtrack('', 0, 0)
        return ans

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans