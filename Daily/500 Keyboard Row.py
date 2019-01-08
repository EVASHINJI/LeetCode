# Url: https://leetcode.com/problems/keyboard-row/
# Related Topics:
# HashTable

# Example:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]


import re
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        for word in words:
            tmp = re.sub("([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$", "", word.lower())
            if not tmp:
                ans.append(word)
        return ans