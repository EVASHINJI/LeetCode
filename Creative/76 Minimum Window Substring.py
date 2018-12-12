# Url: https://leetcode.com/problems/minimum-window-substring/
# Related Topics:
# String HashTable TwoPointers

# Example:
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"

# Creative
# TwoPointers, didn't care about the element specifit location
# and maintain a location queue of chars,
# only focus on whether finish the target in the range of TwoPointers


from collections import Counter
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target = Counter(t)
        todo = set(target.keys())
        left = 0
        start, end = -1, len(s)
        for right, c in enumerate(s):
            if c in target:
                target[c] -= 1
                if target[c] <= 0 and c in todo:
                    todo.remove(c)
                if len(todo) == 0:
                    while s[left] not in target or target[s[left]] < 0:
                        if s[left] in target:
                            target[s[left]] += 1
                        left += 1
                    if right - left < end - start:
                        start, end = left, right
                    target[s[left]] += 1
                    todo.add(s[left])
                    left += 1
        if start == -1:
            return ""
        return s[start:end+1]
                        
                    