# Url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Related Topics:
# String BackTracking

# Example:
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []
        ans = ['']
        for d in digits:
            tmp = []
            for a in ans:
                for m in mapping[d]:
                    tmp.append(a + m)
            ans = tmp
        return ans